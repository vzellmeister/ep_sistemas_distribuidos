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
print("Requesting nothing...")
tm_start = time.time()
stub.DoSomething(void_pb2.Empty())
tm_end = time.time()
print('Nothing done [%s]' % (tm_end - tm_start))