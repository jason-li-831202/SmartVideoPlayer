# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mediapipe/calculators/util/landmark_projection_calculator.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Mediapipe/calculators/util/landmark_projection_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n?Mediapipe/calculators/util/landmark_projection_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xa3\x01\n#LandmarkProjectionCalculatorOptions\x12\x1e\n\x0fignore_rotation\x18\x01 \x01(\x08:\x05\x66\x61lse2\\\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf4\xf8\xca} \x01(\x0b\x32..mediapipe.LandmarkProjectionCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LANDMARKPROJECTIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='LandmarkProjectionCalculatorOptions',
  full_name='mediapipe.LandmarkProjectionCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ignore_rotation', full_name='mediapipe.LandmarkProjectionCalculatorOptions.ignore_rotation', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.LandmarkProjectionCalculatorOptions.ext', index=0,
      number=263371892, type=11, cpp_type=10, label=1,
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
  serialized_start=117,
  serialized_end=280,
)

DESCRIPTOR.message_types_by_name['LandmarkProjectionCalculatorOptions'] = _LANDMARKPROJECTIONCALCULATOROPTIONS

LandmarkProjectionCalculatorOptions = _reflection.GeneratedProtocolMessageType('LandmarkProjectionCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _LANDMARKPROJECTIONCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.util.landmark_projection_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.LandmarkProjectionCalculatorOptions)
  ))
_sym_db.RegisterMessage(LandmarkProjectionCalculatorOptions)

_LANDMARKPROJECTIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _LANDMARKPROJECTIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_LANDMARKPROJECTIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
