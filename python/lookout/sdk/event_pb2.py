# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lookout/sdk/event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bblfsh.github.com.gogo.protobuf.gogoproto import gogo_pb2 as github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lookout/sdk/event.proto',
  package='pb',
  syntax='proto3',
  serialized_pb=_b('\n\x17lookout/sdk/event.proto\x12\x02pb\x1a-github.com/gogo/protobuf/gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"d\n\x0e\x43ommitRevision\x12(\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x14.pb.ReferencePointerB\x04\xc8\xde\x1f\x00\x12(\n\x04head\x18\x02 \x01(\x0b\x32\x14.pb.ReferencePointerB\x04\xc8\xde\x1f\x00\"\xa9\x01\n\x10ReferencePointer\x12:\n\x17internal_repository_url\x18\x01 \x01(\tB\x19\xe2\xde\x1f\x15InternalRepositoryURL\x12K\n\x0ereference_name\x18\x02 \x01(\tB3\xfa\xde\x1f/gopkg.in/src-d/go-git.v4/plumbing.ReferenceName\x12\x0c\n\x04hash\x18\x03 \x01(\t\"\x94\x02\n\tPushEvent\x12\x10\n\x08provider\x18\x01 \x01(\t\x12#\n\x0binternal_id\x18\x02 \x01(\tB\x0e\xe2\xde\x1f\nInternalID\x12\x38\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x0f\n\x07\x63ommits\x18\x04 \x01(\r\x12\x18\n\x10\x64istinct_commits\x18\x05 \x01(\r\x12\x34\n\rconfiguration\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xc8\xde\x1f\x00\x12\x35\n\x0f\x63ommit_revision\x18\x07 \x01(\x0b\x32\x12.pb.CommitRevisionB\x08\xc8\xde\x1f\x00\xd0\xde\x1f\x01\"\xa6\x03\n\x0bReviewEvent\x12\x10\n\x08provider\x18\x01 \x01(\t\x12#\n\x0binternal_id\x18\x02 \x01(\tB\x0e\xe2\xde\x1f\nInternalID\x12\x38\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x38\n\nupdated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x12\x14\n\x0cis_mergeable\x18\x05 \x01(\x08\x12*\n\x06source\x18\x08 \x01(\x0b\x32\x14.pb.ReferencePointerB\x04\xc8\xde\x1f\x00\x12\x34\n\rconfiguration\x18\n \x01(\x0b\x32\x17.google.protobuf.StructB\x04\xc8\xde\x1f\x00\x12\'\n\rrepository_id\x18\x0b \x01(\rB\x10\xe2\xde\x1f\x0cRepositoryID\x12\x0e\n\x06number\x18\x0c \x01(\r\x12\x35\n\x0f\x63ommit_revision\x18\x07 \x01(\x0b\x32\x12.pb.CommitRevisionB\x08\xc8\xde\x1f\x00\xd0\xde\x1f\x01:\x04\xe0\xa1\x1f\x00\x42\x04\xc8\xe1\x1e\x00\x62\x06proto3')
  ,
  dependencies=[github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_COMMITREVISION = _descriptor.Descriptor(
  name='CommitRevision',
  full_name='pb.CommitRevision',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='pb.CommitRevision.base', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head', full_name='pb.CommitRevision.head', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
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
  serialized_start=141,
  serialized_end=241,
)


_REFERENCEPOINTER = _descriptor.Descriptor(
  name='ReferencePointer',
  full_name='pb.ReferencePointer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='internal_repository_url', full_name='pb.ReferencePointer.internal_repository_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\025InternalRepositoryURL')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='pb.ReferencePointer.reference_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\336\037/gopkg.in/src-d/go-git.v4/plumbing.ReferenceName')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='pb.ReferencePointer.hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=244,
  serialized_end=413,
)


_PUSHEVENT = _descriptor.Descriptor(
  name='PushEvent',
  full_name='pb.PushEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='pb.PushEvent.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_id', full_name='pb.PushEvent.internal_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\nInternalID')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='pb.PushEvent.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commits', full_name='pb.PushEvent.commits', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distinct_commits', full_name='pb.PushEvent.distinct_commits', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configuration', full_name='pb.PushEvent.configuration', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_revision', full_name='pb.PushEvent.commit_revision', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\320\336\037\001')), file=DESCRIPTOR),
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
  serialized_start=416,
  serialized_end=692,
)


_REVIEWEVENT = _descriptor.Descriptor(
  name='ReviewEvent',
  full_name='pb.ReviewEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='pb.ReviewEvent.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_id', full_name='pb.ReviewEvent.internal_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\nInternalID')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='pb.ReviewEvent.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='pb.ReviewEvent.updated_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_mergeable', full_name='pb.ReviewEvent.is_mergeable', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='pb.ReviewEvent.source', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configuration', full_name='pb.ReviewEvent.configuration', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repository_id', full_name='pb.ReviewEvent.repository_id', index=7,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\014RepositoryID')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='pb.ReviewEvent.number', index=8,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_revision', full_name='pb.ReviewEvent.commit_revision', index=9,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\320\336\037\001')), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\340\241\037\000')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=695,
  serialized_end=1117,
)

_COMMITREVISION.fields_by_name['base'].message_type = _REFERENCEPOINTER
_COMMITREVISION.fields_by_name['head'].message_type = _REFERENCEPOINTER
_PUSHEVENT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PUSHEVENT.fields_by_name['configuration'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_PUSHEVENT.fields_by_name['commit_revision'].message_type = _COMMITREVISION
_REVIEWEVENT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REVIEWEVENT.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_REVIEWEVENT.fields_by_name['source'].message_type = _REFERENCEPOINTER
_REVIEWEVENT.fields_by_name['configuration'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_REVIEWEVENT.fields_by_name['commit_revision'].message_type = _COMMITREVISION
DESCRIPTOR.message_types_by_name['CommitRevision'] = _COMMITREVISION
DESCRIPTOR.message_types_by_name['ReferencePointer'] = _REFERENCEPOINTER
DESCRIPTOR.message_types_by_name['PushEvent'] = _PUSHEVENT
DESCRIPTOR.message_types_by_name['ReviewEvent'] = _REVIEWEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommitRevision = _reflection.GeneratedProtocolMessageType('CommitRevision', (_message.Message,), dict(
  DESCRIPTOR = _COMMITREVISION,
  __module__ = 'lookout.sdk.event_pb2'
  # @@protoc_insertion_point(class_scope:pb.CommitRevision)
  ))
_sym_db.RegisterMessage(CommitRevision)

ReferencePointer = _reflection.GeneratedProtocolMessageType('ReferencePointer', (_message.Message,), dict(
  DESCRIPTOR = _REFERENCEPOINTER,
  __module__ = 'lookout.sdk.event_pb2'
  # @@protoc_insertion_point(class_scope:pb.ReferencePointer)
  ))
_sym_db.RegisterMessage(ReferencePointer)

PushEvent = _reflection.GeneratedProtocolMessageType('PushEvent', (_message.Message,), dict(
  DESCRIPTOR = _PUSHEVENT,
  __module__ = 'lookout.sdk.event_pb2'
  # @@protoc_insertion_point(class_scope:pb.PushEvent)
  ))
_sym_db.RegisterMessage(PushEvent)

ReviewEvent = _reflection.GeneratedProtocolMessageType('ReviewEvent', (_message.Message,), dict(
  DESCRIPTOR = _REVIEWEVENT,
  __module__ = 'lookout.sdk.event_pb2'
  # @@protoc_insertion_point(class_scope:pb.ReviewEvent)
  ))
_sym_db.RegisterMessage(ReviewEvent)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\310\341\036\000'))
_COMMITREVISION.fields_by_name['base'].has_options = True
_COMMITREVISION.fields_by_name['base']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_COMMITREVISION.fields_by_name['head'].has_options = True
_COMMITREVISION.fields_by_name['head']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_REFERENCEPOINTER.fields_by_name['internal_repository_url'].has_options = True
_REFERENCEPOINTER.fields_by_name['internal_repository_url']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\025InternalRepositoryURL'))
_REFERENCEPOINTER.fields_by_name['reference_name'].has_options = True
_REFERENCEPOINTER.fields_by_name['reference_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\336\037/gopkg.in/src-d/go-git.v4/plumbing.ReferenceName'))
_PUSHEVENT.fields_by_name['internal_id'].has_options = True
_PUSHEVENT.fields_by_name['internal_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\nInternalID'))
_PUSHEVENT.fields_by_name['created_at'].has_options = True
_PUSHEVENT.fields_by_name['created_at']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001'))
_PUSHEVENT.fields_by_name['configuration'].has_options = True
_PUSHEVENT.fields_by_name['configuration']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_PUSHEVENT.fields_by_name['commit_revision'].has_options = True
_PUSHEVENT.fields_by_name['commit_revision']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\320\336\037\001'))
_REVIEWEVENT.fields_by_name['internal_id'].has_options = True
_REVIEWEVENT.fields_by_name['internal_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\nInternalID'))
_REVIEWEVENT.fields_by_name['created_at'].has_options = True
_REVIEWEVENT.fields_by_name['created_at']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001'))
_REVIEWEVENT.fields_by_name['updated_at'].has_options = True
_REVIEWEVENT.fields_by_name['updated_at']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\220\337\037\001'))
_REVIEWEVENT.fields_by_name['source'].has_options = True
_REVIEWEVENT.fields_by_name['source']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_REVIEWEVENT.fields_by_name['configuration'].has_options = True
_REVIEWEVENT.fields_by_name['configuration']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000'))
_REVIEWEVENT.fields_by_name['repository_id'].has_options = True
_REVIEWEVENT.fields_by_name['repository_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\342\336\037\014RepositoryID'))
_REVIEWEVENT.fields_by_name['commit_revision'].has_options = True
_REVIEWEVENT.fields_by_name['commit_revision']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\310\336\037\000\320\336\037\001'))
_REVIEWEVENT.has_options = True
_REVIEWEVENT._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\340\241\037\000'))
# @@protoc_insertion_point(module_scope)
