# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mediapipe/calculators/image/set_alpha_calculator.proto

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
  name='Mediapipe/calculators/image/set_alpha_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n6Mediapipe/calculators/image/set_alpha_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x88\x01\n\x19SetAlphaCalculatorOptions\x12\x17\n\x0b\x61lpha_value\x18\x01 \x01(\x11:\x02-12R\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xa7\xe1\xd4w \x01(\x0b\x32$.mediapipe.SetAlphaCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SETALPHACALCULATOROPTIONS = _descriptor.Descriptor(
  name='SetAlphaCalculatorOptions',
  full_name='mediapipe.SetAlphaCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='alpha_value', full_name='mediapipe.SetAlphaCalculatorOptions.alpha_value', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.SetAlphaCalculatorOptions.ext', index=0,
      number=250949799, type=11, cpp_type=10, label=1,
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
  serialized_start=108,
  serialized_end=244,
)

DESCRIPTOR.message_types_by_name['SetAlphaCalculatorOptions'] = _SETALPHACALCULATOROPTIONS

SetAlphaCalculatorOptions = _reflection.GeneratedProtocolMessageType('SetAlphaCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _SETALPHACALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.image.set_alpha_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.SetAlphaCalculatorOptions)
  ))
_sym_db.RegisterMessage(SetAlphaCalculatorOptions)

_SETALPHACALCULATOROPTIONS.extensions_by_name['ext'].message_type = _SETALPHACALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_SETALPHACALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
