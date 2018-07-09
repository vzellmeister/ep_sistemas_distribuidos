import rpyc
import time
import random


# Connect to server
conn = rpyc.connect("localhost", 50051, config={'allow_all_attrs':True})

# Loop for 10 tests
for i in range(0, 10):
    tm_start = time.time()
    conn.root.doSomething() # call upon remote server
    tm_end = time.time()
    print(tm_end - tm_start) # print time taken