# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mediapipe/modules/face_geometry/protos/mesh_3d.proto

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
  name='Mediapipe/modules/face_geometry/protos/mesh_3d.proto',
  package='mediapipe.face_geometry',
  syntax='proto2',
  serialized_pb=_b('\n4Mediapipe/modules/face_geometry/protos/mesh_3d.proto\x12\x17mediapipe.face_geometry\"\xf9\x01\n\x06Mesh3d\x12?\n\x0bvertex_type\x18\x01 \x01(\x0e\x32*.mediapipe.face_geometry.Mesh3d.VertexType\x12\x45\n\x0eprimitive_type\x18\x02 \x01(\x0e\x32-.mediapipe.face_geometry.Mesh3d.PrimitiveType\x12\x15\n\rvertex_buffer\x18\x03 \x03(\x02\x12\x14\n\x0cindex_buffer\x18\x04 \x03(\r\"\x1b\n\nVertexType\x12\r\n\tVERTEX_PT\x10\x00\"\x1d\n\rPrimitiveType\x12\x0c\n\x08TRIANGLE\x10\x00\x42\x38\n)com.google.mediapipe.modules.facegeometryB\x0bMesh3dProto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MESH3D_VERTEXTYPE = _descriptor.EnumDescriptor(
  name='VertexType',
  full_name='mediapipe.face_geometry.Mesh3d.VertexType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERTEX_PT', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=273,
  serialized_end=300,
)
_sym_db.RegisterEnumDescriptor(_MESH3D_VERTEXTYPE)

_MESH3D_PRIMITIVETYPE = _descriptor.EnumDescriptor(
  name='PrimitiveType',
  full_name='mediapipe.face_geometry.Mesh3d.PrimitiveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRIANGLE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=302,
  serialized_end=331,
)
_sym_db.RegisterEnumDescriptor(_MESH3D_PRIMITIVETYPE)


_MESH3D = _descriptor.Descriptor(
  name='Mesh3d',
  full_name='mediapipe.face_geometry.Mesh3d',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertex_type', full_name='mediapipe.face_geometry.Mesh3d.vertex_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primitive_type', full_name='mediapipe.face_geometry.Mesh3d.primitive_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertex_buffer', full_name='mediapipe.face_geometry.Mesh3d.vertex_buffer', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index_buffer', full_name='mediapipe.face_geometry.Mesh3d.index_buffer', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESH3D_VERTEXTYPE,
    _MESH3D_PRIMITIVETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=331,
)

_MESH3D.fields_by_name['vertex_type'].enum_type = _MESH3D_VERTEXTYPE
_MESH3D.fields_by_name['primitive_type'].enum_type = _MESH3D_PRIMITIVETYPE
_MESH3D_VERTEXTYPE.containing_type = _MESH3D
_MESH3D_PRIMITIVETYPE.containing_type = _MESH3D
DESCRIPTOR.message_types_by_name['Mesh3d'] = _MESH3D

Mesh3d = _reflection.GeneratedProtocolMessageType('Mesh3d', (_message.Message,), dict(
  DESCRIPTOR = _MESH3D,
  __module__ = 'mediapipe.modules.face_geometry.protos.mesh_3d_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.face_geometry.Mesh3d)
  ))
_sym_db.RegisterMessage(Mesh3d)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n)com.google.mediapipe.modules.facegeometryB\013Mesh3dProto'))
# @@protoc_insertion_point(module_scope)
