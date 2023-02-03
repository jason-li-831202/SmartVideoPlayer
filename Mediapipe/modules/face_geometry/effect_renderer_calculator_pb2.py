# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mediapipe/modules/face_geometry/effect_renderer_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Mediapipe/modules/face_geometry/effect_renderer_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n@Mediapipe/modules/face_geometry/effect_renderer_calculator.proto\x12\tmediapipe\x1a,mediapipe/framework/calculator_options.proto\"\xce\x01\n+FaceGeometryEffectRendererCalculatorOptions\x12\x1b\n\x13\x65\x66\x66\x65\x63t_texture_path\x18\x01 \x01(\t\x12\x1b\n\x13\x65\x66\x66\x65\x63t_mesh_3d_path\x18\x02 \x01(\t2e\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf0\xd9\xac\x9a\x01 \x01(\x0b\x32\x36.mediapipe.FaceGeometryEffectRendererCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__options__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FACEGEOMETRYEFFECTRENDERERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='FaceGeometryEffectRendererCalculatorOptions',
  full_name='mediapipe.FaceGeometryEffectRendererCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='effect_texture_path', full_name='mediapipe.FaceGeometryEffectRendererCalculatorOptions.effect_texture_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effect_mesh_3d_path', full_name='mediapipe.FaceGeometryEffectRendererCalculatorOptions.effect_mesh_3d_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.FaceGeometryEffectRendererCalculatorOptions.ext', index=0,
      number=323693808, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=332,
)

DESCRIPTOR.message_types_by_name['FaceGeometryEffectRendererCalculatorOptions'] = _FACEGEOMETRYEFFECTRENDERERCALCULATOROPTIONS

FaceGeometryEffectRendererCalculatorOptions = _reflection.GeneratedProtocolMessageType('FaceGeometryEffectRendererCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _FACEGEOMETRYEFFECTRENDERERCALCULATOROPTIONS,
  __module__ = 'mediapipe.modules.face_geometry.effect_renderer_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FaceGeometryEffectRendererCalculatorOptions)
  ))
_sym_db.RegisterMessage(FaceGeometryEffectRendererCalculatorOptions)

_FACEGEOMETRYEFFECTRENDERERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _FACEGEOMETRYEFFECTRENDERERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_FACEGEOMETRYEFFECTRENDERERCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
