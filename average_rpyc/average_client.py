import rpyc
import time
import random

def run():
    conn = rpyc.connect("localhost", 50051, config={'allow_all_attrs':True})
    print("Generating [8] array...")
    l = [random.randint(-2000000000,2000000000) for e in range(8)]

    print("Averaging...")

    tm_start = time.time()
    l = conn.root.avgit(l)
    tm_end = time.time()
    print('Averaged [%s]' % (tm_end - tm_start))


if __name__ == '__main__':
    run()
