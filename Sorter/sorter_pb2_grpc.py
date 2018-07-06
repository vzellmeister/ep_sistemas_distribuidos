# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sorter_pb2 as sorter__pb2


class StringFormatterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.sort = channel.unary_unary(
        '/StringFormatter/sort',
        request_serializer=sorter__pb2.sortRequest.SerializeToString,
        response_deserializer=sorter__pb2.sortReply.FromString,
        )


class StringFormatterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def sort(self, request, context):
    """orders elements
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StringFormatterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sort': grpc.unary_unary_rpc_method_handler(
          servicer.sort,
          request_deserializer=sorter__pb2.sortRequest.FromString,
          response_serializer=sorter__pb2.sortReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'StringFormatter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))