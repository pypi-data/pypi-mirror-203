

customize_service = """
import logging
from taichu_serve import Service

logger = logging.getLogger(__name__)


class TestService(Service):
    def __init__(self, model_path):
        super(TestService, self).__init__(model_path)
        logger.info("self.model_path: %s",
                    model_path)

    def _preprocess(self, input_data, context):
        logger.info('enter _preprocess')
        
        return input_data

    def _inference(self, preprocessed_result, context):
        logger.info('enter _inference')
        
        return preprocessed_result

    def _postprocess(self, inference_result, context):
        logger.info('enter _postprocess')

        return inference_result

    def _warmup(self):
        logger.info('warmup finished')
"""

config_ini = """
[rate-limiter]
max_concurrent_requests = 2

[server]
grpc_port = 8889
http_port = 8888
grpc_only = False
instances_num = 1
"""

requirements = """
taichu-serve
"""

http_client = """
import requests

url = "http://localhost:8888/v2/models/TestService/versions/1/infer"

payload = {
  "parameters": {
    "str": "str",
    "float": 1.222,
    "bool": True
  }
}

response = requests.request("POST", url, json=payload)
print(response.text)
"""

stream_grpc_client = """
import grpc
import taichu_serve.grpc_predict_v2_pb2 as grpc_predict_v2_pb2
import taichu_serve.grpc_predict_v2_pb2_grpc as grpc_predict_v2_pb2_grpc


def guide_list_features(stub):
    num = 5

    while True:

        def generator():
            for i in range(num):
                req = grpc_predict_v2_pb2.ModelInferRequest()
                req.model_name = 'testservice'
                req.model_version = '1'

                req.parameters['input'].bool_param = True
                yield req

        resp = stub.ModelStreamInfer(generator())
        for feature in resp:
            print(feature)


def run():
    with grpc.insecure_channel('localhost:8889') as channel:
        stub = grpc_predict_v2_pb2_grpc.GRPCInferenceServiceStub(channel)
        print("-------------- ListFeatures --------------")
        guide_list_features(stub)


if __name__ == '__main__':
    run()
"""

grpc_clent = """
import grpc
import taichu_serve.grpc_predict_v2_pb2 as grpc_predict_v2_pb2
import taichu_serve.grpc_predict_v2_pb2_grpc as grpc_predict_v2_pb2_grpc


def run():
    conn = grpc.insecure_channel('localhost:8889')
    client = grpc_predict_v2_pb2_grpc.GRPCInferenceServiceStub(channel=conn)

    req = grpc_predict_v2_pb2.ModelInferRequest()
    req.model_name = 'testservice'
    req.model_version = '1'
    req.parameters['boo_var'].bool_param = True
    req.parameters['float_var'].float_param = 12.3432
    req.parameters['str_var'].string_param = 'str'

    respnse = client.ModelInfer(req)
    print("received:", respnse)


if __name__ == '__main__':
    run()
"""


