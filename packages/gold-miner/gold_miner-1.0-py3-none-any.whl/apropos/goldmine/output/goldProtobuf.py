import sys
import uuid
import os
from logging import debug, info, warning, error, critical  # must be after scapy

from apropos.goldmine.output import GoldOutput

sys.path.append(
    os.path.join(os.path.dirname(__file__), "../..", "searchlight-protobuf-api/python")
)
sys.path.append(
    os.path.join(
        os.path.dirname(__file__), "../..", "searchlight-protobuf-api/protobuf/src"
    )
)
sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "searchlight-protobuf-api/python")
)
sys.path.append(
    os.path.join(
        os.path.dirname(__file__), "..", "searchlight-protobuf-api/protobuf/src"
    )
)
import apropos.goldmine.searchlight_protobuf_api.flow_pb2 as Flow


class GoldProtobuf(GoldOutput):
    "mimics a protobuf server by dropping protobuf content into a file/unix-socket"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output_file = kwargs.get("output_file")
        self.threshold = kwargs.get("threshold")
        self.subscription = kwargs.get("subscriptions")
        self.out_file_handle = kwargs.get("output_file_handle")

        # if we were passed a file instead of a raw socket to write
        if not self.out_file_handle and self.output_file:
            self.out_file_handle = open(self.output_file, "wb")
        self.have_recorded = {}
        self.count = 0

    def create_flow(self, row):
        flow = Flow.Flow()
        id = str(uuid.uuid4())
        flow.id = id
        debug(f"creating flow id: {id}: {self.count}")
        self.count += 1

        if isinstance(row[1], tuple):
            flow.flow_ntuple.add().protocol = row[1][0]
            if row[1][1].find(":") > -1:
                flow.flow_ntuple.add().src_ip.v6 = row[1][1]
                flow.flow_ntuple.add().dst_ip.v6 = row[1][2]
            else:
                flow.flow_ntuple.add().src_ip.v4 = row[1][1]
                flow.flow_ntuple.add().dst_ip.v4 = row[1][2]
            if len(row[1]) == 4:  # ESP
                t = flow.flow_ntuple.add()
                t.other.attribute_name = "ipsec"
                t.other.attribute_value.type_url = "SPI"
                t.other.attribute_value.value = bytes(str(row[1][3]), "utf-8")
            if len(row[1]) > 4:  # 5-tuple
                flow.flow_ntuple.add().src_port = row[1][3]
                flow.flow_ntuple.add().dst_port = row[1][4]
        else:  # at least send something?
            t = flow.flow_ntuple.add()
            t.other.attribute_name = "unknown"
            t.other.attribute_value.type_url = "unknown"
            t.other.attribute_value.value = bytes(self.str_spi(row[1]), "utf-8")

        # t.other.attribute_value = row[1]
        return flow

    def output(self, analysis_results, packet_number, tunnel_count, subscriptions):
        for row in analysis_results:
            (timestamp, spi, label, value, packets) = row

            if label in self.have_recorded:
                continue  # XXX: eventually allow dropping below threshold again

            # calculate the confidence value
            confidence = self.calculate_confidence(label, value)

            # report if we're above threshold
            if confidence >= self.threshold:

                # don't report again
                id = str(uuid.uuid4())
                self.have_recorded[label] = id

                flow = self.create_flow(row)

                debug(flow)
                self.out_file_handle.write(flow.SerializeToString())
                self.out_file_handle.flush()

    def close(self):
        self.out_file_handle.close()
