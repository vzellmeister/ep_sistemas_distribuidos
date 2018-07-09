import grpc
import time
import random

# import the generated classes
import sorter_pb2
import sorter_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = sorter_pb2_grpc.SorterStub(channel)

# create a valid request message
print("Generating [1000] array...")
l = [random.uniform(0,1) for e in range(1000)]
req = sorter_pb2.List()
req.values.extend(l)

# make the call
print("Sorting...")
tm_start = time.time()
response = stub.sortit(req)
tm_end = time.time()
print('Sorted [%s]' % (tm_end - tm_start))