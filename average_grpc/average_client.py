import grpc
import time
import random

# import the generated classes
import average_pb2
import average_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = average_pb2_grpc.AveragerStub(channel)

# create a valid request message
print("Generating [8] array...")
l = [random.randint(-2000000000,2000000000) for e in range(8)]
req = average_pb2.List()
req.values.extend(l)

# make the call
print("Averaging...")
tm_start = time.time()
response = stub.avgit(req)
tm_end = time.time()
print('Averaged [%s]' % (tm_end - tm_start))