# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mediapipe/modules/objectron/calculators/object.proto

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
  name='Mediapipe/modules/objectron/calculators/object.proto',
  package='mediapipe',
  syntax='proto3',
  serialized_pb=_b('\n4Mediapipe/modules/objectron/calculators/object.proto\x12\tmediapipe\"d\n\x08KeyPoint\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\x19\n\x11\x63onfidence_radius\x18\x04 \x01(\x02\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0e\n\x06hidden\x18\x06 \x01(\x08\"\xd0\x02\n\x06Object\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12$\n\x04type\x18\x03 \x01(\x0e\x32\x16.mediapipe.Object.Type\x12\x10\n\x08rotation\x18\x04 \x03(\x02\x12\x13\n\x0btranslation\x18\x05 \x03(\x02\x12\r\n\x05scale\x18\x06 \x03(\x02\x12&\n\tkeypoints\x18\x07 \x03(\x0b\x32\x13.mediapipe.KeyPoint\x12(\n\x06method\x18\x08 \x01(\x0e\x32\x18.mediapipe.Object.Method\":\n\x04Type\x12\x12\n\x0eUNDEFINED_TYPE\x10\x00\x12\x10\n\x0c\x42OUNDING_BOX\x10\x01\x12\x0c\n\x08SKELETON\x10\x02\">\n\x06Method\x12\x12\n\x0eUNKNOWN_METHOD\x10\x00\x12\x0e\n\nANNOTATION\x10\x01\x12\x10\n\x0c\x41UGMENTATION\x10\x02\"$\n\x04\x45\x64ge\x12\x0e\n\x06source\x18\x01 \x01(\x05\x12\x0c\n\x04sink\x18\x02 \x01(\x05\"\x80\x01\n\x08Skeleton\x12\x1a\n\x12reference_keypoint\x18\x01 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12&\n\tkeypoints\x18\x03 \x03(\x0b\x32\x13.mediapipe.KeyPoint\x12\x1e\n\x05\x65\x64ges\x18\x04 \x03(\x0b\x32\x0f.mediapipe.Edge\"0\n\tSkeletons\x12#\n\x06object\x18\x01 \x03(\x0b\x32\x13.mediapipe.Skeletonb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OBJECT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='mediapipe.Object.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOUNDING_BOX', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKELETON', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=384,
  serialized_end=442,
)
_sym_db.RegisterEnumDescriptor(_OBJECT_TYPE)

_OBJECT_METHOD = _descriptor.EnumDescriptor(
  name='Method',
  full_name='mediapipe.Object.Method',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_METHOD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANNOTATION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUGMENTATION', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=444,
  serialized_end=506,
)
_sym_db.RegisterEnumDescriptor(_OBJECT_METHOD)


_KEYPOINT = _descriptor.Descriptor(
  name='KeyPoint',
  full_name='mediapipe.KeyPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='mediapipe.KeyPoint.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='mediapipe.KeyPoint.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='mediapipe.KeyPoint.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence_radius', full_name='mediapipe.KeyPoint.confidence_radius', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='mediapipe.KeyPoint.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hidden', full_name='mediapipe.KeyPoint.hidden', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=67,
  serialized_end=167,
)


_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='mediapipe.Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mediapipe.Object.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='mediapipe.Object.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='mediapipe.Object.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='mediapipe.Object.rotation', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='translation', full_name='mediapipe.Object.translation', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='mediapipe.Object.scale', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoints', full_name='mediapipe.Object.keypoints', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='method', full_name='mediapipe.Object.method', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBJECT_TYPE,
    _OBJECT_METHOD,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=506,
)


_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='mediapipe.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='mediapipe.Edge.source', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sink', full_name='mediapipe.Edge.sink', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=508,
  serialized_end=544,
)


_SKELETON = _descriptor.Descriptor(
  name='Skeleton',
  full_name='mediapipe.Skeleton',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_keypoint', full_name='mediapipe.Skeleton.reference_keypoint', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='mediapipe.Skeleton.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keypoints', full_name='mediapipe.Skeleton.keypoints', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edges', full_name='mediapipe.Skeleton.edges', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=547,
  serialized_end=675,
)


_SKELETONS = _descriptor.Descriptor(
  name='Skeletons',
  full_name='mediapipe.Skeletons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object', full_name='mediapipe.Skeletons.object', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=677,
  serialized_end=725,
)

_OBJECT.fields_by_name['type'].enum_type = _OBJECT_TYPE
_OBJECT.fields_by_name['keypoints'].message_type = _KEYPOINT
_OBJECT.fields_by_name['method'].enum_type = _OBJECT_METHOD
_OBJECT_TYPE.containing_type = _OBJECT
_OBJECT_METHOD.containing_type = _OBJECT
_SKELETON.fields_by_name['keypoints'].message_type = _KEYPOINT
_SKELETON.fields_by_name['edges'].message_type = _EDGE
_SKELETONS.fields_by_name['object'].message_type = _SKELETON
DESCRIPTOR.message_types_by_name['KeyPoint'] = _KEYPOINT
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['Skeleton'] = _SKELETON
DESCRIPTOR.message_types_by_name['Skeletons'] = _SKELETONS

KeyPoint = _reflection.GeneratedProtocolMessageType('KeyPoint', (_message.Message,), dict(
  DESCRIPTOR = _KEYPOINT,
  __module__ = 'mediapipe.modules.objectron.calculators.object_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.KeyPoint)
  ))
_sym_db.RegisterMessage(KeyPoint)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), dict(
  DESCRIPTOR = _OBJECT,
  __module__ = 'mediapipe.modules.objectron.calculators.object_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Object)
  ))
_sym_db.RegisterMessage(Object)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(
  DESCRIPTOR = _EDGE,
  __module__ = 'mediapipe.modules.objectron.calculators.object_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Edge)
  ))
_sym_db.RegisterMessage(Edge)

Skeleton = _reflection.GeneratedProtocolMessageType('Skeleton', (_message.Message,), dict(
  DESCRIPTOR = _SKELETON,
  __module__ = 'mediapipe.modules.objectron.calculators.object_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Skeleton)
  ))
_sym_db.RegisterMessage(Skeleton)

Skeletons = _reflection.GeneratedProtocolMessageType('Skeletons', (_message.Message,), dict(
  DESCRIPTOR = _SKELETONS,
  __module__ = 'mediapipe.modules.objectron.calculators.object_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Skeletons)
  ))
_sym_db.RegisterMessage(Skeletons)


# @@protoc_insertion_point(module_scope)
