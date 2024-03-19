# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import warehouse_pb2 as warehouse__pb2


class WarehouseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getWarehouseData = channel.unary_unary(
                '/warehouse.WarehouseService/getWarehouseData',
                request_serializer=warehouse__pb2.WarehouseRequest.SerializeToString,
                response_deserializer=warehouse__pb2.WarehouseResponse.FromString,
                )
        self.HealthCheck = channel.unary_unary(
                '/warehouse.WarehouseService/HealthCheck',
                request_serializer=warehouse__pb2.PingRequest.SerializeToString,
                response_deserializer=warehouse__pb2.PingResponse.FromString,
                )


class WarehouseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getWarehouseData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HealthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WarehouseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getWarehouseData': grpc.unary_unary_rpc_method_handler(
                    servicer.getWarehouseData,
                    request_deserializer=warehouse__pb2.WarehouseRequest.FromString,
                    response_serializer=warehouse__pb2.WarehouseResponse.SerializeToString,
            ),
            'HealthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.HealthCheck,
                    request_deserializer=warehouse__pb2.PingRequest.FromString,
                    response_serializer=warehouse__pb2.PingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'warehouse.WarehouseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WarehouseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getWarehouseData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warehouse.WarehouseService/getWarehouseData',
            warehouse__pb2.WarehouseRequest.SerializeToString,
            warehouse__pb2.WarehouseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HealthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warehouse.WarehouseService/HealthCheck',
            warehouse__pb2.PingRequest.SerializeToString,
            warehouse__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class HealthCheckServiceStub(object):
    """EKv

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/warehouse.HealthCheckService/Ping',
                request_serializer=warehouse__pb2.PingRequest.SerializeToString,
                response_deserializer=warehouse__pb2.PingResponse.FromString,
                )


class HealthCheckServiceServicer(object):
    """EKv

    """

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HealthCheckServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=warehouse__pb2.PingRequest.FromString,
                    response_serializer=warehouse__pb2.PingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'warehouse.HealthCheckService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HealthCheckService(object):
    """EKv

    """

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/warehouse.HealthCheckService/Ping',
            warehouse__pb2.PingRequest.SerializeToString,
            warehouse__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)