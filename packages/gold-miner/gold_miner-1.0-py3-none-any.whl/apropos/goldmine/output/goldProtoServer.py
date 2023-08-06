import sys
import os
import grpc
import queue
import time

from logging import debug, info, warning, error, critical  # must be after scapy

sys.path.append(
    os.path.join(
        os.path.dirname(__file__), "../../../..", "searchlight-protobuf-api/python"
    )
)
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "../../../..",
        "searchlight-protobuf-api/protobuf/src",
    )
)

import apropos.goldmine.searchlight_protobuf_api.flowsubservice_pb2 as flowsubservice_pb2
import apropos.goldmine.searchlight_protobuf_api.flowsubservice_pb2_grpc as flowsubservice_pb2_grpc
import apropos.goldmine.searchlight_protobuf_api.subscription_pb2 as subscription_pb2


class GoldProtoServer(flowsubservice_pb2_grpc.FlowSubscriptionService):
    "Listens for subscriptions and responds to GetVersion, Subscribe, ... requests"

    def __init__(self, bind_address, subscription_queue=None, default_confidence=None):
        self.count = 0
        self.subscription_queue = subscription_queue
        self.our_queue = None
        self.our_queues = {}
        self.bind_address = bind_address
        self.default_confidence = default_confidence
        pass

    def GetVersion(self, request, context):
        debug(f"GetVersion: {request}")
        r = flowsubservice_pb2.GetVersionResponse()
        r.endpoint_id = "wes"
        r.api_version = "2"
        r.this_endpoint.contact_url = "https://www.isi.edu/"
        r.this_endpoint.service_type = (
            1  # XXX: flowsubservice_pb2.ServiceType.APROPOS_SERVICE
        )
        r.this_endpoint.attribute.add().service_version = "2"
        r.this_endpoint.attribute.add().node_location.v4 = self.bind_address
        r.this_endpoint.attribute.add().description = "in a broom closet"
        debug(r)
        return r

    def Subscribe(self, request, context):
        """Listens for subscriptions, and creates a subscription
        for each application filter it receives."""
        client = request.client_uuid
        sub_id = f"apropos_rc_sub{self.count}"
        self.count += 1

        debug(f"Subscribe received: {request}")
        for af in request.spec.application_filters:
            subscription = {
                "type": "subscribe",
                "name": af.name.name,
                "score": af.score.score,
                "client": client,
                "sub_id": sub_id,
                "found": {},
            }
            if not subscription["score"]:
                subscription["score"] = self.default_confidence
            self.subscription_queue.put(subscription)

        subscription = {
            "type": "subscribe",
            "client": client,
            "sub_id": sub_id,
            "found": {},
            "score": self.default_confidence,
        }

        gold_names = []
        for af in request.spec.application_filters:
            gold_names.append(af.name.name)
            if af.score.score:
                subscription["score"] = af.score.score
        subscription["names"] = gold_names

        ipaddresses = []
        for ef in request.spec.entity_filters:
            # XXX: check that label is src_ip
            for tup in ef.tuples:
                print(tup.value.value)
                ipaddresses.append(tup.value.value.decode())
            if ef.score.score:
                subscription["score"] = ef.score.score
        subscription["ipaddresses"] = ipaddresses

        self.subscription_queue.put(subscription)
        info(f"subscription received: {subscription}")

        r = flowsubservice_pb2.SubscribeResponse()
        r.id.name = sub_id
        return r

    def GetMatchingFlows(self, request, context):
        "Creates a queue for each received client, and sends it to the subscription queue"
        client = request.client_uuid

        info(f"GetMatchingFlows: {request} {self.our_queue}")

        if client not in self.our_queues:
            self.our_queues[client] = queue.Queue()

        self.subscription_queue.put(
            {
                "type": "get_matching_flows",
                "client": client,
                "queue": self.our_queues[client],
            }
        )  # XXX: confidence

        while True:
            event = False
            for client in self.our_queues:
                if not self.our_queues[client].empty():
                    event = self.our_queues[client].get()
                    break

            if event is False:
                time.sleep(0.1)
                continue

            if event is None:
                debug("termination request -- quitting")
                break

            debug(f"got matching flow from queue: {event}")
            debug(f"got matching flow/type from queue: {type(event)}")

            response = flowsubservice_pb2.GetMatchingFlowsResponse()
            response.flow.CopyFrom(event)

            yield response
