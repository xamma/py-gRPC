import grpc
from concurrent import futures
import greeter_pb2
import greeter_pb2_grpc

class InMemoryDatabase:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.id] = item

    def get_item(self, item_id):
        return self.items.get(item_id)

    def list_items(self):
        return list(self.items.values())

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False

class Greeter(greeter_pb2_grpc.GreeterServicer):
    def __init__(self, db):
        self.db = db

    def SayHello(self, request, context):
        print(f"Received greeting request from {request.name}")
        return greeter_pb2.HelloReply(message=f"Hello, {request.name}!")

    def AddItem(self, request, context):
        print(f"Received item request: ID={request.id}, Name={request.name}, Quantity={request.quantity}")
        self.db.add_item(request)
        return greeter_pb2.ItemReply(id=request.id, name=request.name, quantity=request.quantity)

    def GetItem(self, request, context):
        print(f"Received item retrieval request for ID={request.id}")
        item = self.db.get_item(request.id)
        if item:
            return greeter_pb2.ItemReply(id=item.id, name=item.name, quantity=item.quantity)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Item not found")
            return greeter_pb2.ItemReply()

    def ListItems(self, request, context):
        print("Received request to list all items")
        items = self.db.list_items()
        return greeter_pb2.ItemList(items=[greeter_pb2.Item(id=item.id, name=item.name, quantity=item.quantity) for item in items])

    def DeleteItem(self, request, context):
        print(f"Received item deletion request for ID={request.id}")
        success = self.db.delete_item(request.id)
        if success:
            return greeter_pb2.Empty()
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Item not found")
            return greeter_pb2.Empty()

def serve():
    db = InMemoryDatabase()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(db), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
