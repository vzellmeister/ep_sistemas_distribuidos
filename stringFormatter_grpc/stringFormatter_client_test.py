from __future__ import print_function

import grpc
import time
import string
import random

# RPC modules
import stringFormatter_pb2
import stringFormatter_pb2_grpc

#==============================================================================
#                                  FUNCTIONS
#==============================================================================
def capitalize(string):
    '''Calls upon server to capitalize all chars in string'''
    return FORMATTER.Upper( stringFormatter_pb2.UpperRequest( upperReqStr=string ) ).upperRepStr

def randStr(size):
    '''Creates string of determined size with all lowercase'''
    return ''.join(random.choice(
                    string.ascii_lowercase +  string.digits
                ) for _ in range(size))

#==============================================================================
#                                  GLOBAL VARS
#==============================================================================
CHANNEL = grpc.insecure_channel('localhost:50051')
FORMATTER = stringFormatter_pb2_grpc.StringFormatterStub(CHANNEL)

#==============================================================================
#                                     MAIN
#==============================================================================
def run():
    for strSz in range(0, 11): # string size for powers of 2, from 0 to 10
        print('\nSIZE %d' % (2 ** strSz))
        for testNum in range (1, 11): # runs 10 tests
            sttTime = time.time() # Get time stamp before executing RPC
            capitalize( randStr(2 ** strSz) ) # execute RPC
            endTime = time.time() # Get time after RPC
            print('TEST %00d: %f' % (testNum, endTime - sttTime))
        
if __name__ == '__main__':
    run()
