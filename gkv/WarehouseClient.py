import time

import grpc
import warehouse_pb2
import warehouse_pb2_grpc

def run():
    #name = "first"
    # Establish a channel with the gRPC server
    with (grpc.insecure_channel('localhost:50022') as channel):
        # Create a stub (client)
        stub = warehouse_pb2_grpc.WarehouseServiceStub(channel)
        healthStub = warehouse_pb2_grpc.HealthCheckServiceStub(channel)


        # Create a request
        request = warehouse_pb2.WarehouseRequest(uuid="cdbe69b5-932b-45d2-9c13-fa408e100cda")

        # Make the call to the server
        response = stub.getWarehouseData(request)

        # Print the response from the server, accessing fields directly
        print("WarehouseClient received response:")
        print(f" Warehouse ID: {response.warehouse_id}")
        print(f" Warehouse Name: {response.warehouse_name}")
        print(f" Warehouse Address: {response.warehouse_address}")
        print(f" Warehouse Postal Code: {response.warehouse_postal_code}")
        print(f" Warehouse City: {response.warehouse_city}")
        print(f" Warehouse Country: {response.warehouse_country}")
        print(f" Timestamp: {response.timestamp}\n")
        # If you want to print product data as well
        for product in response.product_data:
            print(f"  Product ID: {product.product_id}")
            print(f"  Product Name: {product.product_name}")
            print(f"  Product Category: {product.product_category}")
            print(f"  Product Quantity: {product.product_quantity}")
            print(f"  Product Unit: {product.product_unit}\n")

        # Respond to a Ping manually as an example
        # response = stub.getWarehouseData(request)
        # .PingResponse(warehouse_pb2.PingRequest(message="Ping"))
        # print(f"Received pong with message: {response.message}")

        while True:
            request = warehouse_pb2.PingRequest(message="Ping")
            response = healthStub.Ping(request)
            # response = healthStub.HealthCheck(request)
            # response = stub.Ping(request)
            # warehouse_pb2.PingRequest(message="Ping")
            print(f"Received pong with message: {response.message}")
            time.sleep(8)

if __name__ == '__main__':
    run()
