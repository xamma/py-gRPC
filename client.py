import grpc
import greeter_pb2
import greeter_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = greeter_pb2_grpc.GreeterStub(channel)

    # Call the SayHello method
    response = stub.SayHello(greeter_pb2.HelloRequest(name='Max'))
    print("Greeter client received: " + response.message)

    # Call the AddItem method
    item = greeter_pb2.Item(id='1', name='Item 2', quantity=16)
    add_item_response = stub.AddItem(item)
    print("Item added: " + add_item_response.id)

    # Call the GetItem method
    get_item_response = stub.GetItem(greeter_pb2.ItemRequest(id='1'))
    print("Item retrieved: " + get_item_response.name + ", Quantity: " + str(get_item_response.quantity))

    # Call the ListItems method
    list_items_response = stub.ListItems(greeter_pb2.Empty())
    print("Items in database:")
    for item in list_items_response.items:
        print(f"ID: {item.id}, Name: {item.name}, Quantity: {item.quantity}")

    # Call the DeleteItem method
    delete_item_response = stub.DeleteItem(greeter_pb2.ItemRequest(id='1'))
    print("Item deleted")

if __name__ == '__main__':
    run()
