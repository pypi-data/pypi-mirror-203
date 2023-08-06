# coding: utf-8
import logging
import os
from concurrent import futures

import grpc

from taichu_serve.grpc_predict_v2_pb2_grpc import add_GRPCInferenceServiceServicer_to_server
from taichu_serve.app import app, init_model_service_instance
from taichu_serve.grpc_server import GrpcModelService, GrpcServerInterceptor
from taichu_serve.settings import parse_args
from taichu_serve.template import config_ini, customize_service, requirements, http_client, stream_grpc_client,grpc_clent

LOGGER = logging.getLogger(__name__)


def init_project(name="project"):
    # 在当前目录下创建项目目录
    if not os.path.exists(name):
        os.mkdir(name)

    with open(os.path.join(name, "customize_service.py"), "w") as f:
        f.write(customize_service)
    print("create customize_service.py done!")

    with open(os.path.join(name, "config.ini"), "w") as f:
        f.write(config_ini)
    print("create config.ini done!")

    with open(os.path.join(name, "requirements.txt"), "w") as f:
        f.write(requirements)
    print("create requirements.txt done!")

    if not os.path.exists(os.path.join(name, 'test')):
        os.mkdir(os.path.join(name, 'test'))

    with open(os.path.join(name, 'test', "http_client.py"), "w") as f:
        f.write(http_client)
    print("create http_client.py done!")

    with open(os.path.join(name, 'test', "stream_grpc_client.py"), "w") as f:
        f.write(stream_grpc_client)
    print("create stream_grpc_client.py done!")

    with open(os.path.join(name, 'test', "grpc_client.py"), "w") as f:
        f.write(grpc_clent)
    print("create grpc_client.py done!")

    print("init project done!")


def cli():
    args = parse_args()
    if args.action == "init":
        init_project()
        return

    init_model_service_instance()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.max_concurrent_requests),
                         maximum_concurrent_rpcs=args.max_concurrent_requests + 5,
                         interceptors=[GrpcServerInterceptor()])

    add_GRPCInferenceServiceServicer_to_server(GrpcModelService(), server)
    server.add_insecure_port(f'[::]:{args.grpc_port}')

    server.start()
    LOGGER.info("grpc server start at port %s", args.grpc_port)

    if args.grpc_only:
        server.wait_for_termination()

    app.run("0.0.0.0", args.http_port)
    return app
