import grpc
import time
import random

# import the generated classes
import void_pb2
import void_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = void_pb2_grpc.DoerStub(channel)

# make the call
for i in range(1, 11):
    tm_start = time.time()
    stub.DoSomething(void_pb2.Empty())
    tm_end = time.time()
    print(tm_end - tm_start)