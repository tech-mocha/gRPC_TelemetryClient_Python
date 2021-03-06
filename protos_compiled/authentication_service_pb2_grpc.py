# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import authentication_service_pb2 as authentication__service__pb2


class LoginStub(object):
  """The Login service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.LoginCheck = channel.unary_unary(
        '/authentication.Login/LoginCheck',
        request_serializer=authentication__service__pb2.LoginRequest.SerializeToString,
        response_deserializer=authentication__service__pb2.LoginReply.FromString,
        )


class LoginServicer(object):
  """The Login service definition.
  """

  def LoginCheck(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LoginServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'LoginCheck': grpc.unary_unary_rpc_method_handler(
          servicer.LoginCheck,
          request_deserializer=authentication__service__pb2.LoginRequest.FromString,
          response_serializer=authentication__service__pb2.LoginReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'authentication.Login', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
