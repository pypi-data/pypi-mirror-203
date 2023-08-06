"""sends a single request to a GPRC server and maybe follows content"""

import os
import sys
import uuid
import grpc
import time

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
from logging import debug, info, warning, error, critical
import logging


def parse_args():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description=__doc__,
        epilog="Exmaple Usage: ",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="get version information from the server",
    )

    parser.add_argument(
        "-s",
        "--subscriptions",
        default=[],
        type=str,
        nargs="*",
        help="List of identifiers to subscribe to.",
    )

    parser.add_argument(
        "-a",
        "--addresses",
        default=[],
        type=str,
        nargs="*",
        help="List of IPv4 or v6 addresses to limit results to",
    )

    parser.add_argument(
        "-c",
        "--confidence",
        default=None,
        type=int,
        help="Confidence level to subscribe at (1-100).",
    )

    parser.add_argument(
        "-I",
        "--include",
        default=None,
        type=str,
        help="A path to search for searchlight API and google proto python files",
    )
    parser.add_argument(
        "--log-level",
        "--ll",
        default="info",
        help="Define the logging verbosity level (debug, info, warning, error, fotal, critical).",
    )

    parser.add_argument("server_address", type=str, help="Server to connect to")

    args = parser.parse_args()

    log_level = args.log_level.upper()
    logging.basicConfig(level=log_level, format="%(levelname)-10s:\t%(message)s")

    if args.include:
        sys.path.append(args.include)
        sys.path.append(os.path.join(args.include, "python"))
        sys.path.append(os.path.join(args.include, "protobuf/src"))

    if not args.subscriptions and not args.version and not args.addresses:
        error("either -v, -s or -a is required")
        exit()

    return args


def main():
    args = parse_args()

    import apropos.goldmine.searchlight_protobuf_api.flowsubservice_pb2_grpc as flowsubservice_pb2_grpc
    import apropos.goldmine.searchlight_protobuf_api.flowsubservice_pb2 as flowsubservice_pb2
    import apropos.goldmine.searchlight_protobuf_api.subscription_pb2 as Subscription

    with grpc.insecure_channel(args.server_address) as server:
        stub = flowsubservice_pb2_grpc.FlowSubscriptionServiceStub(server)
        info("started server stub")

        if args.version:
            version = stub.GetVersion(flowsubservice_pb2.GetVersionRequest())
            print(version)
            exit()

        if args.subscriptions or args.addresses:
            client = str(uuid.uuid4())

            # send our subscription info
            subreq = flowsubservice_pb2.SubscribeRequest()
            subreq.client_uuid = client

            for app in args.subscriptions:
                af = subreq.spec.application_filters.add()
                af.name.name = app
                af.description = f"apps matching {app}"
                if args.confidence:
                    af.score.score = args.confidence

            for address in args.addresses:
                ef = subreq.spec.entity_filters.add()
                ef.name.name = address
                ef.description = f"entities matching {address}"
                newip = ef.tuples.add()
                newip.label = "src_ip"
                newip.value.value = bytes(address, "utf-8")
                if args.confidence:
                    ef.score.score = args.confidence

            info(subreq)
            response = stub.Subscribe(subreq)
            info(response)

            # now start following it
            while True:
                request = flowsubservice_pb2.GetMatchingFlowsRequest()
                request.client_uuid = client
                responses = stub.GetMatchingFlows(request)

                print("==========")
                for response in responses:
                    print("---------- received flow:")
                    print(response)
                time.sleep(0.5)


if __name__ == "__main__":
    main()
