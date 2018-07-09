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
"""The Python implementation of a crappy string formatter."""

from concurrent import futures
import time

import grpc

import stringFormatter_pb2
import stringFormatter_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Formatter(stringFormatter_pb2_grpc.StringFormatterServicer):

    # Makes all characters in string upper case
    def Upper(self, request, context):
        print('Upper request received at: %s' % (time.strftime('%H:%M:%S', time.gmtime())))
        return stringFormatter_pb2.UpperReply( upperRepStr=str( request.upperReqStr ).upper() )

    # Makes all characters in string lower case
    def Lower(self, request, context):
        print('Lower request received at: %s' % (time.strftime('%H:%M:%S', time.gmtime())))
        return stringFormatter_pb2.LowerReply( lowerRepStr=str( request.lowerReqStr ).lower() )

    # Makes first character in each word upper case, all other characters lower case
    def Proper(self, request, context):
        print('Proper request received at: %s' % (time.strftime('%H:%M:%S', time.gmtime())))
        return stringFormatter_pb2.ProperReply( propRepStr=str( request.propReqStr ).title() )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stringFormatter_pb2_grpc.add_StringFormatterServicer_to_server(Formatter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()