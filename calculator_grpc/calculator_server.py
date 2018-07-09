# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time

import grpc

import calculator_pb2
import calculator_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(calculator_pb2_grpc.CalculatorServicer):

    def Addition(self, request, context):
        print('Received Addition request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        return calculator_pb2.AdditionReply(resultAdd=request.fstOperandAdd + request.scdOperandAdd)

    def Subtraction(self, request, context):
        print('Received Subtraction request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        return calculator_pb2.SubtractionReply(resultSub=request.fstOperandSub - request.scdOperandSub)

    def Multiplication(self, request, context):
        print('Received Multiplication request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        return calculator_pb2.MultiplicationReply(resultMul=request.fstOperandMul * request.scdOperandMul)
    
    def Division(self, request, context):
        print('Received Division request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        return calculator_pb2.DivisionReply(resultDiv=request.fstOperandDiv / request.scdOperandDiv)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()