import uuid
import time
from logging import debug, info, warning, error, critical  # must be after scapy

from apropos.goldmine.output import GoldOutput
from apropos.goldmine.output.goldProtobuf import GoldProtobuf


class GoldQueue(GoldProtobuf):
    """Continually outputs results to a queue headed back to the client
    for flows that match a subscription specification."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.queue = kwargs.get("queue")
        self.raw_values = kwargs.get("raw_values")
        self.client = kwargs.get("client")
        self.subscriptions = kwargs.get("subscriptions")
        del kwargs["queue"]

    # XXX: need to do finds per identifier
    def output(self, analysis_results, packet_number, tunnel_count, subscriptions):
        for row in analysis_results:
            (timestamp, identifier, label, value, packets) = row

            # calculate the confidence value
            confidence = 100 * self.calculate_confidence(label, value)

            if not self.raw_values:
                value = self.calculate_confidence(label, value)

            debug(f"QUEUE: {label} {confidence}")
            for client in subscriptions:
                # get the inner dict
                for subscription in subscriptions[client]:
                    debug(
                        f"  subscription: {subscription} {client} {subscription['sub_id']} found={subscription['found']}"
                    )
                    # XXX: need to report multiple times
                    # need to check other match types
                    debug(subscription)

                    # don't report again -- TODO: this should be
                    # smarter to watch for flows that go away,
                    # retransmits ever N seconds, high/low water
                    # marks, etc
                    if identifier in subscription["found"]:
                        continue
                    subscription["found"][identifier] = True

                    valid = True
                    # check the confidence score
                    if (
                        subscription.get("score", None)
                        and confidence < subscription["score"]
                    ):
                        # current threshold not met
                        valid = False

                    # check the application names we want for this sub
                    for name in subscription["names"]:
                        # this requires ANDing all names, which seems wrong but is the spec
                        if label != name:
                            debug("  no match")
                            valid = False

                    if not valid:
                        continue

                    # check IP to/from addresses against the subscription list
                    for address in subscription["ipaddresses"]:
                        if identifier[1] != address and identifier[2] != address:
                            valid = False

                    if not valid:
                        continue

                    flow = self.create_flow(row)
                    # XXX: we only report one subscription, spec calls for multiple
                    sub = flow.matching_subscriptions.add()
                    sub.name = subscription["sub_id"]
                    sub.score.score = int(confidence)

                    app = flow.matching_applications.add()
                    app.name.name = label
                    app.description = f"application detected: {label}"
                    app.score.score = int(confidence)

                    # XXX: need to report original times of first packet,
                    # and update last seen
                    t = time.time()
                    secs = int(t)
                    nanos = int(1000000000 * (t - int(t)))
                    flow.first_seen_time.seconds = secs
                    flow.first_seen_time.nanos = nanos
                    flow.last_seen_time.seconds = secs
                    flow.last_seen_time.nanos = nanos

                    # XXX: add other components besides the flow

                    info("transmitting flow identified")
                    info(flow)
                    info(self.queue)

                    self.queue.put(flow)

    def close(self):
        pass
