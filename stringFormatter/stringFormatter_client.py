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

GET_STR_PROMPT = ('Please insert string to operate:\n')

# All options; keys are numbers, sub dictionary contains titles and functions (via lambda)
OPTIONS ={
    '1': {'title': 'Upper', 'function': (
            lambda string: FORMATTER.Upper( stringFormatter_pb2.UpperRequest( upperReqStr=string ) ).upperRepStr
            )},
    '2': {'title': 'Lower', 'function': (
            lambda string: FORMATTER.Lower( stringFormatter_pb2.LowerRequest( lowerReqStr=string) ).lowerRepStr
    )},
    '3': {'title': 'Capitalize', 'function': (
            lambda string: FORMATTER.Proper( stringFormatter_pb2.ProperRequest( propReqStr=string) ).propRepStr
    )}
}

#==============================================================================
#                                     MAIN
#==============================================================================
def run():
    # Get input string
    string = str(input(GET_STR_PROMPT)) # Get value

    print()
    print(  )

    while True:
        chosenOption = str(input(
            'What would you like to do with the string "%s"?\n%s\n' % (
                string,
                ('\n').join([k + ' - ' + v['title'] for k, v in OPTIONS.items()])
            )
        ))
        if chosenOption in OPTIONS.keys():
            print('Option: %s' % (chosenOption))
            break
        print('This is not a valid option. Please choose from the above.')

    sttTime = time.time()
    rString = OPTIONS[chosenOption]['function'](string)
    endTime = time.time()
    print('RESULT: "%s" %s' % (rString, endTime - sttTime))

if __name__ == '__main__':
    run()
