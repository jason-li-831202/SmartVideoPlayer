# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mediapipe/calculators/util/timed_box_list_id_to_label_calculator.proto

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
  name='Mediapipe/calculators/util/timed_box_list_id_to_label_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\nFMediapipe/calculators/util/timed_box_list_id_to_label_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xa2\x01\n&TimedBoxListIdToLabelCalculatorOptions\x12\x16\n\x0elabel_map_path\x18\x01 \x01(\t2`\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xe6\xa1\xfa\x8d\x01 \x01(\x0b\x32\x31.mediapipe.TimedBoxListIdToLabelCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TIMEDBOXLISTIDTOLABELCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TimedBoxListIdToLabelCalculatorOptions',
  full_name='mediapipe.TimedBoxListIdToLabelCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label_map_path', full_name='mediapipe.TimedBoxListIdToLabelCalculatorOptions.label_map_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TimedBoxListIdToLabelCalculatorOptions.ext', index=0,
      number=297701606, type=11, cpp_type=10, label=1,
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
  serialized_start=124,
  serialized_end=286,
)

DESCRIPTOR.message_types_by_name['TimedBoxListIdToLabelCalculatorOptions'] = _TIMEDBOXLISTIDTOLABELCALCULATOROPTIONS

TimedBoxListIdToLabelCalculatorOptions = _reflection.GeneratedProtocolMessageType('TimedBoxListIdToLabelCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _TIMEDBOXLISTIDTOLABELCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.util.timed_box_list_id_to_label_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TimedBoxListIdToLabelCalculatorOptions)
  ))
_sym_db.RegisterMessage(TimedBoxListIdToLabelCalculatorOptions)

_TIMEDBOXLISTIDTOLABELCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TIMEDBOXLISTIDTOLABELCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TIMEDBOXLISTIDTOLABELCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
