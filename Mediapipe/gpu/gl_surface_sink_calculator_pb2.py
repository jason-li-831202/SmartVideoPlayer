# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/gpu/gl_surface_sink_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
from Mediapipe.gpu import scale_mode_pb2 as mediapipe_dot_gpu_dot_scale__mode__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/gpu/gl_surface_sink_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n.mediapipe/gpu/gl_surface_sink_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x1emediapipe/gpu/scale_mode.proto\"\xae\x01\n\x1eGlSurfaceSinkCalculatorOptions\x12\x33\n\x10\x66rame_scale_mode\x18\x01 \x01(\x0e\x32\x19.mediapipe.ScaleMode.Mode2W\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8a\xfb\x83t \x01(\x0b\x32).mediapipe.GlSurfaceSinkCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_gpu_dot_scale__mode__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GLSURFACESINKCALCULATOROPTIONS = _descriptor.Descriptor(
  name='GlSurfaceSinkCalculatorOptions',
  full_name='mediapipe.GlSurfaceSinkCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_scale_mode', full_name='mediapipe.GlSurfaceSinkCalculatorOptions.frame_scale_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.GlSurfaceSinkCalculatorOptions.ext', index=0,
      number=243334538, type=11, cpp_type=10, label=1,
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
  serialized_start=132,
  serialized_end=306,
)

_GLSURFACESINKCALCULATOROPTIONS.fields_by_name['frame_scale_mode'].enum_type = mediapipe_dot_gpu_dot_scale__mode__pb2._SCALEMODE_MODE
DESCRIPTOR.message_types_by_name['GlSurfaceSinkCalculatorOptions'] = _GLSURFACESINKCALCULATOROPTIONS

GlSurfaceSinkCalculatorOptions = _reflection.GeneratedProtocolMessageType('GlSurfaceSinkCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _GLSURFACESINKCALCULATOROPTIONS,
  __module__ = 'mediapipe.gpu.gl_surface_sink_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.GlSurfaceSinkCalculatorOptions)
  ))
_sym_db.RegisterMessage(GlSurfaceSinkCalculatorOptions)

_GLSURFACESINKCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _GLSURFACESINKCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_GLSURFACESINKCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
