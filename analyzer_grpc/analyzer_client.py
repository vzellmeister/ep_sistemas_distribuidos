import grpc
import time
import random

# import the generated classes
import analyzer_pb2
import analyzer_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = analyzer_pb2_grpc.AnalyzerStub(channel)

# create a valid request message
print("Generating data...")
data = analyzer_pb2.Data()
data.id = random.randint(1,10)
data.username = "Username"
data.level.bonus = random.randint(100,1000)
data.level.multiplier = random.uniform(1, 1.75)
for i in range(0,100):
    play = data.plays.add()
    play.time = random.uniform(0.2, 3.5)
    play.precision = random.uniform(.6,.98)

# make the call
print("Calling server...")
tm_start = time.time()
response = stub.score(data)
tm_end = time.time()
print('Score %d [%s]' % (response.score, tm_end - tm_start))

