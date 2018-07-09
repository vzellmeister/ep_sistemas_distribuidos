import time
import random

class Sorter:
    def sort( self, list ):
        return list.sort()


def run():
    S = Sorter()
    l = [random.uniform(0,1) for e in range(1000)]

    tm_start = time.time()
    l = S.sort(l)
    tm_end = time.time()
    print('Sorted [%s]' % (tm_end - tm_start))


if __name__ == '__main__':
    run()