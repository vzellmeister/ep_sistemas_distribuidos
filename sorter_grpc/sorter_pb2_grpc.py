# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sorter_pb2 as sorter__pb2


class SorterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.sortit = channel.unary_unary(
        '/Sorter/sortit',
        request_serializer=sorter__pb2.List.SerializeToString,
        response_deserializer=sorter__pb2.List.FromString,
        )


class SorterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def sortit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SorterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sortit': grpc.unary_unary_rpc_method_handler(
          servicer.sortit,
          request_deserializer=sorter__pb2.List.FromString,
          response_serializer=sorter__pb2.List.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Sorter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))