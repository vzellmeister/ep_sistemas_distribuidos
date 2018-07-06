# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
import time
import random

# RPC modules
import sorter_pb2
import sorter_pb2_grpc
import pickle
import string

#==============================================================================
#                                   FUNCTIONS
#==============================================================================
def sort(obj):
    if not isinstance(obj, list):
        raise TypeError('Sorter only accepts list objects. Passed object was of type: "%s"' % (obj.__class__.__name__ ))
    return SORTER.sort( sorter_pb2.sortRequest(sortReq= pickle.dumps(obj) ) ).sortRep

def getElements(l, sz):
    print('manual generation %d' % (sz))
    for i in range(0, sz):
        l.append( input(PROMPT_ADD_ITEM.replace('<i>', '%2d' % (i + 1))) )

def rndElements(l, sz):
    print('random generation %d' % (sz))
    for i in range(0, sz):
        l.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(1, 100))))


#==============================================================================
#                                  GLOBAL VARS
#==============================================================================
CHANNEL = grpc.insecure_channel('localhost:50051')
SORTER = sorter_pb2_grpc.StringFormatterStub(CHANNEL)
PROMPT_LIST_SIZE = 'Please set the number of items for your list:\n'
PROMPT_ADD_ITEM = 'Please set item number <i>:\n'
PROMPT_TYPE_OF_LIST = 'Would you like to:\n[1] manually set the elements of your list OR\n[2] randomly generate the elements of your list?   '
LIST_TYPE_CHOICE = ''
LIST_TYPES = {
    '1': {
        'name': 'manual',
        'prompt': 'manually declare elements of list',
        'function': getElements
    },
    '2': {
        'name': 'automatic',
        'prompt': 'randomly generate all elements',
        'function': rndElements
    }
}
LIST_SIZE = 0
LIST = []



#==============================================================================
#                                     MAIN
#==============================================================================
def run():
    

    while(True):
        LIST_TYPE_CHOICE = input(PROMPT_TYPE_OF_LIST)
        if LIST_TYPE_CHOICE in LIST_TYPES.keys():
            print(LIST_TYPE_CHOICE.upper())
            break
        print('Invalid choice.')

    print('List of type %s chosen' % (LIST_TYPES[LIST_TYPE_CHOICE]['name']))

    while(True):
        LIST_SIZE = str( input(PROMPT_LIST_SIZE) ) # get list size
        if LIST_SIZE.isnumeric:
            LIST_SIZE = int(LIST_SIZE)
            break
        print('Invalid number.')
    
    print('List will be %d elements long' % (LIST_SIZE)) # Get list size

    LIST_TYPES[LIST_TYPE_CHOICE]['function'](LIST, LIST_SIZE) # Populate list
    
    print('LISTA:\n%s' % (str(LIST)))
    print('========================')
    LIST = sort(LIST)
    print('LISTA ORDENADA:\n%s' % (str(LIST)))



if __name__ == '__main__':
    run()
