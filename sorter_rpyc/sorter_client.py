import rpyc
import time
import random

def run():
    conn = rpyc.connect("localhost", 50051, config={'allow_all_attrs':True})
    print("Generating [1000] array...")
    l = [random.uniform(0,1) for e in range(1000)]

    print("Sorting...")

    tm_start = time.time()
    l = conn.root.sortit(l)
    tm_end = time.time()
    print('Sorted [%s]' % (tm_end - tm_start))


if __name__ == '__main__':
    run()
