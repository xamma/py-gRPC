# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greeter.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rgreeter.proto\x12\x07greeter\"2\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"7\n\tItemReply\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\"\x19\n\x0bItemRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"(\n\x08ItemList\x12\x1c\n\x05items\x18\x01 \x03(\x0b\x32\r.greeter.Item2\x92\x02\n\x07Greeter\x12\x38\n\x08SayHello\x12\x15.greeter.HelloRequest\x1a\x13.greeter.HelloReply\"\x00\x12.\n\x07\x41\x64\x64Item\x12\r.greeter.Item\x1a\x12.greeter.ItemReply\"\x00\x12\x35\n\x07GetItem\x12\x14.greeter.ItemRequest\x1a\x12.greeter.ItemReply\"\x00\x12\x30\n\tListItems\x12\x0e.greeter.Empty\x1a\x11.greeter.ItemList\"\x00\x12\x34\n\nDeleteItem\x12\x14.greeter.ItemRequest\x1a\x0e.greeter.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greeter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ITEM']._serialized_start=26
  _globals['_ITEM']._serialized_end=76
  _globals['_HELLOREQUEST']._serialized_start=78
  _globals['_HELLOREQUEST']._serialized_end=106
  _globals['_HELLOREPLY']._serialized_start=108
  _globals['_HELLOREPLY']._serialized_end=137
  _globals['_ITEMREPLY']._serialized_start=139
  _globals['_ITEMREPLY']._serialized_end=194
  _globals['_ITEMREQUEST']._serialized_start=196
  _globals['_ITEMREQUEST']._serialized_end=221
  _globals['_EMPTY']._serialized_start=223
  _globals['_EMPTY']._serialized_end=230
  _globals['_ITEMLIST']._serialized_start=232
  _globals['_ITEMLIST']._serialized_end=272
  _globals['_GREETER']._serialized_start=275
  _globals['_GREETER']._serialized_end=549
# @@protoc_insertion_point(module_scope)
