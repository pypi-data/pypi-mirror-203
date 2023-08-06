# import click
# import logging
# from concurrent import futures
#
# import grpc
#
# from taichu_serve.grpc_predict_v2_pb2_grpc import add_GRPCInferenceServiceServicer_to_server
# from taichu_serve.app import app, init_model_service_instance
# from taichu_serve.error_code import ModelNotFoundError, TooManyRequestsError
# from taichu_serve.grpc_server import GrpcModelService, GrpcServerInterceptor
# from taichu_serve.ratelimiter import semaphore
#
#
#
#
# @click.group()
# def cli():
#     pass
#
#
# @click.command()
# @click.argument('name')
# def init_project(name):
#     click.echo('Hello %s!' % name)
#
#     # parser.add_argument('--grpc_port', action="store", default=8889, type=int)
#     # parser.add_argument('--http_port', action="store", default=8888, type=int)
#     # parser.add_argument('--grpc_only', action="store", default=False, type=bool)
#     # parser.add_argument('--model_path', action="store", default='./', type=str)
#     # parser.add_argument('--service_file', action="store", default='customize_service.py', type=str)
#     # parser.add_argument('--max_concurrent_requests', action="store", default=1, type=int)
#     # parser.add_argument('--instances_num', action="store", default=1, type=int)
#     #
#
#
# @click.command()
# @click.option('--grpc_port', default=8889, type=int)
# @click.option('--http_port', default=8888, type=int)
# @click.option('--grpc_only', default=False, type=bool)
# @click.option('--model_path', default='./', type=str)
# @click.option('--service_file', default='customize_service.py', type=str)
# @click.option('--max_concurrent_requests', default=1, type=int)
# @click.option('--instances_num', default=1, type=int)
# def serve(grpc_port, http_port, grpc_only, model_path, service_file, max_concurrent_requests, instances_num):
#
#
#
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_concurrent_requests),
#                          maximum_concurrent_rpcs=max_concurrent_requests + 5,
#                          interceptors=[GrpcServerInterceptor()])
#
#     add_GRPCInferenceServiceServicer_to_server(GrpcModelService(), server)
#     server.add_insecure_port(f'[::]:{args.grpc_port}')
#
#     server.start()
#     LOGGER.info("grpc server start at port %s", args.grpc_port)
#     # from gevent.pywsgi import WSGIServer
#     # http_server = WSGIServer(("0.0.0.0", args.http_port), app)
#     # LOGGER.info("http server start at port %s", args.http_port)
#     #
#     # http_server.serve_forever()
#     if args.grpc_only:
#         server.wait_for_termination()
#
#     app.run("0.0.0.0", args.http_port)
#
#
# cli.add_command(init_project, name='init')
# cli.add_command(serve, name='serve')
#
# if __name__ == '__main__':
#     cli()
