import rpyc
import time
import random


# Connect to server
conn = rpyc.connect("localhost", 50051, config={'allow_all_attrs':True})

# make the call
print("Requesting nothing...")
tm_start = time.time()
conn.root.doSomething
tm_end = time.time()
print('Nothing done [%s]' % (tm_end - tm_start))