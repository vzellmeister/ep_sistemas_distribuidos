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

# RPC modules
import stringFormatter_pb2
import stringFormatter_pb2_grpc

#==============================================================================
#                                  GLOBAL VARS
#==============================================================================
CHANNEL = grpc.insecure_channel('localhost:50051')
FORMATTER = stringFormatter_pb2_grpc.StringFormatterStub(CHANNEL)
CHOICE_PROMPT = ('''
What would you like to do with your string?
    1 - Upper
    2 - Lower
    3 - Capitalize
''')
GET_STR_PROMPT = ('Please insert string to operate:\n')

#==============================================================================
#                                     MAIN
#==============================================================================
def run():
    # Get input string
    string = str(input(GET_STR_PROMPT)) # Get value
    print('STRING = "%s"' % (string))

    print('======================================================================')

    while True:
        chosenOption = str( input(CHOICE_PROMPT) )
        if chosenOption.isnumeric() and int(chosenOption) >= 1 and int(chosenOption) <= 3:
            print('')


if __name__ == '__main__':
    run()
