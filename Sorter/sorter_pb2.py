# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sorter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sorter.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0csorter.proto\"\x1e\n\x0bsortRequest\x12\x0f\n\x07sortReq\x18\x01 \x01(\t\"\x1c\n\tsortReply\x12\x0f\n\x07sortRep\x18\x01 \x01(\t23\n\x0fStringFormatter\x12 \n\x04sort\x12\x0c.sortRequest\x1a\n.sortReplyb\x06proto3')
)




_SORTREQUEST = _descriptor.Descriptor(
  name='sortRequest',
  full_name='sortRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sortReq', full_name='sortRequest.sortReq', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=46,
)


_SORTREPLY = _descriptor.Descriptor(
  name='sortReply',
  full_name='sortReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sortRep', full_name='sortReply.sortRep', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=76,
)

DESCRIPTOR.message_types_by_name['sortRequest'] = _SORTREQUEST
DESCRIPTOR.message_types_by_name['sortReply'] = _SORTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

sortRequest = _reflection.GeneratedProtocolMessageType('sortRequest', (_message.Message,), dict(
  DESCRIPTOR = _SORTREQUEST,
  __module__ = 'sorter_pb2'
  # @@protoc_insertion_point(class_scope:sortRequest)
  ))
_sym_db.RegisterMessage(sortRequest)

sortReply = _reflection.GeneratedProtocolMessageType('sortReply', (_message.Message,), dict(
  DESCRIPTOR = _SORTREPLY,
  __module__ = 'sorter_pb2'
  # @@protoc_insertion_point(class_scope:sortReply)
  ))
_sym_db.RegisterMessage(sortReply)



_STRINGFORMATTER = _descriptor.ServiceDescriptor(
  name='StringFormatter',
  full_name='StringFormatter',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=78,
  serialized_end=129,
  methods=[
  _descriptor.MethodDescriptor(
    name='sort',
    full_name='StringFormatter.sort',
    index=0,
    containing_service=None,
    input_type=_SORTREQUEST,
    output_type=_SORTREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STRINGFORMATTER)

DESCRIPTOR.services_by_name['StringFormatter'] = _STRINGFORMATTER

# @@protoc_insertion_point(module_scope)