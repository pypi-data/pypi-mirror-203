# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: log.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tlog.proto\x12\x06\x65vents\"\xc5\x01\n\nLogMessage\x12\x0f\n\x07message\x18\x01 \x02(\x0c\x12\x34\n\x0cmessage_type\x18\x02 \x02(\x0e\x32\x1e.events.LogMessage.MessageType\x12\x11\n\ttimestamp\x18\x03 \x02(\x03\x12\x0e\n\x06\x61pp_id\x18\x04 \x01(\t\x12\x13\n\x0bsource_type\x18\x05 \x01(\t\x12\x17\n\x0fsource_instance\x18\x06 \x01(\t\"\x1f\n\x0bMessageType\x12\x07\n\x03OUT\x10\x01\x12\x07\n\x03\x45RR\x10\x02\x42/\n!org.cloudfoundry.dropsonde.eventsB\nLogFactory')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'log_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!org.cloudfoundry.dropsonde.eventsB\nLogFactory'
  _LOGMESSAGE._serialized_start=22
  _LOGMESSAGE._serialized_end=219
  _LOGMESSAGE_MESSAGETYPE._serialized_start=188
  _LOGMESSAGE_MESSAGETYPE._serialized_end=219
# @@protoc_insertion_point(module_scope)
