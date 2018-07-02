# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import stringFormatter_pb2 as stringFormatter__pb2


class StringFormatterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Upper = channel.unary_unary(
        '/StringFormatter/Upper',
        request_serializer=stringFormatter__pb2.UpperRequest.SerializeToString,
        response_deserializer=stringFormatter__pb2.UpperReply.FromString,
        )
    self.Lower = channel.unary_unary(
        '/StringFormatter/Lower',
        request_serializer=stringFormatter__pb2.LowerRequest.SerializeToString,
        response_deserializer=stringFormatter__pb2.LowerReply.FromString,
        )
    self.Proper = channel.unary_unary(
        '/StringFormatter/Proper',
        request_serializer=stringFormatter__pb2.ProperRequest.SerializeToString,
        response_deserializer=stringFormatter__pb2.ProperReply.FromString,
        )


class StringFormatterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Upper(self, request, context):
    """makes all chars in string upper case 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Lower(self, request, context):
    """makes all chars in string lower case
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Proper(self, request, context):
    """makes first char in every word upper case, all other chars lower case
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StringFormatterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Upper': grpc.unary_unary_rpc_method_handler(
          servicer.Upper,
          request_deserializer=stringFormatter__pb2.UpperRequest.FromString,
          response_serializer=stringFormatter__pb2.UpperReply.SerializeToString,
      ),
      'Lower': grpc.unary_unary_rpc_method_handler(
          servicer.Lower,
          request_deserializer=stringFormatter__pb2.LowerRequest.FromString,
          response_serializer=stringFormatter__pb2.LowerReply.SerializeToString,
      ),
      'Proper': grpc.unary_unary_rpc_method_handler(
          servicer.Proper,
          request_deserializer=stringFormatter__pb2.ProperRequest.FromString,
          response_serializer=stringFormatter__pb2.ProperReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'StringFormatter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
