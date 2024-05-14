# gRPC with Python
Small example on how to setup an gRPC (remote procedure call) server and interact with it via an client.  
Lets you write items to an in-memory Database and gives you a psersonalized greeting :)  

In contrast to a "traditional" REST Api, every RPC method in the gRPC service is accessible via a unique endpoint.  
These endpoints are called by the clients using gRPC stubs.  

## Files overview
The file **greeter_pb2** contains message classes for your Protocol Buffers message types.  
The file **greeter_pb2_grpc** contains gRPC client and server classes for your service definitions.  
Both are generated automatically from the compiling of the protobuf file **greeter.proto**.  

## Some terms in the world of gRPC
In gRPC, a "stub" is a client-side representation of the remote service. It acts as a local proxy for the remote methods provided by the gRPC server.  

When you define gRPC services and messages using Protocol Buffers, you compile them using the protoc compiler, which generates client and server code in your chosen language. The generated client code includes a stub class, which provides methods corresponding to the RPCs defined in your service.  

Here's what the stub does:  

Method Invocation: The stub provides methods that correspond to the RPCs defined in your service. For example, if your service defines a method called AddItem, the stub will provide a method with the same name on the client side.  

Serialization and Deserialization: When you invoke a method on the stub, it handles serializing the request message into bytes (marshalling) and sending it over the network to the gRPC server. It also handles deserializing the response bytes back into the corresponding message object (unmarshalling).  

Network Communication: The stub abstracts away the network communication details. You don't need to worry about low-level networking code; you simply call methods on the stub, and it handles the communication with the remote server.  

Asynchronous and Synchronous Calls: Depending on your language and preferences, the stub may provide both synchronous and asynchronous versions of the RPC methods. Synchronous calls block until a response is received, while asynchronous calls return a future or a callback, allowing you to continue other tasks while waiting for the response.  

In summary, the stub is a crucial component in gRPC client-side programming. It provides a convenient and high-level interface for interacting with remote gRPC services.  

## How to run
We first need to compile the protobuf file
```
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. greeter.proto
```

Start the server
```
python server.py 
```

In another terminal:  
Send requests
```
python client.py
```