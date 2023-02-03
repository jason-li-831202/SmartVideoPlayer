# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mediapipe/calculators/util/non_max_suppression_calculator.proto

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
  name='Mediapipe/calculators/util/non_max_suppression_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n?Mediapipe/calculators/util/non_max_suppression_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xf5\x04\n\"NonMaxSuppressionCalculatorOptions\x12 \n\x15num_detection_streams\x18\x01 \x01(\x05:\x01\x31\x12\x1e\n\x12max_num_detections\x18\x02 \x01(\x05:\x02-1\x12\x1f\n\x13min_score_threshold\x18\x06 \x01(\x02:\x02-1\x12$\n\x19min_suppression_threshold\x18\x03 \x01(\x02:\x01\x31\x12X\n\x0coverlap_type\x18\x04 \x01(\x0e\x32\x39.mediapipe.NonMaxSuppressionCalculatorOptions.OverlapType:\x07JACCARD\x12\x1f\n\x17return_empty_detections\x18\x05 \x01(\x08\x12V\n\talgorithm\x18\x07 \x01(\x0e\x32:.mediapipe.NonMaxSuppressionCalculatorOptions.NmsAlgorithm:\x07\x44\x45\x46\x41ULT\"k\n\x0bOverlapType\x12\x1c\n\x18UNSPECIFIED_OVERLAP_TYPE\x10\x00\x12\x0b\n\x07JACCARD\x10\x01\x12\x14\n\x10MODIFIED_JACCARD\x10\x02\x12\x1b\n\x17INTERSECTION_OVER_UNION\x10\x03\")\n\x0cNmsAlgorithm\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08WEIGHTED\x10\x01\x32[\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xbc\xa8\xb4\x1a \x01(\x0b\x32-.mediapipe.NonMaxSuppressionCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_NONMAXSUPPRESSIONCALCULATOROPTIONS_OVERLAPTYPE = _descriptor.EnumDescriptor(
  name='OverlapType',
  full_name='mediapipe.NonMaxSuppressionCalculatorOptions.OverlapType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_OVERLAP_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JACCARD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODIFIED_JACCARD', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERSECTION_OVER_UNION', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=503,
  serialized_end=610,
)
_sym_db.RegisterEnumDescriptor(_NONMAXSUPPRESSIONCALCULATOROPTIONS_OVERLAPTYPE)

_NONMAXSUPPRESSIONCALCULATOROPTIONS_NMSALGORITHM = _descriptor.EnumDescriptor(
  name='NmsAlgorithm',
  full_name='mediapipe.NonMaxSuppressionCalculatorOptions.NmsAlgorithm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEIGHTED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=612,
  serialized_end=653,
)
_sym_db.RegisterEnumDescriptor(_NONMAXSUPPRESSIONCALCULATOROPTIONS_NMSALGORITHM)


_NONMAXSUPPRESSIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='NonMaxSuppressionCalculatorOptions',
  full_name='mediapipe.NonMaxSuppressionCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_detection_streams', full_name='mediapipe.NonMaxSuppressionCalculatorOptions.num_detection_streams', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_num_detections', full_name='mediapipe.NonMaxSuppressionCalculatorOptions.max_num_detections', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_score_threshold', full_name='mediapipe.NonMaxSuppressionCalculatorOptions.min_score_threshold', index=2,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_suppression_threshold', full_name='mediapipe.NonMaxSuppressionCalculatorOptions.min_suppression_threshold', index=3,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='overlap_type', full_name='mediapipe.NonMaxSuppressionCalculatorOptions.overlap_type', index=4,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='return_empty_detections', full_name='mediapipe.NonMaxSuppressionCalculatorOptions.return_empty_detections', index=5,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='mediapipe.NonMaxSuppressionCalculatorOptions.algorithm', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.NonMaxSuppressionCalculatorOptions.ext', index=0,
      number=55383100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
    _NONMAXSUPPRESSIONCALCULATOROPTIONS_OVERLAPTYPE,
    _NONMAXSUPPRESSIONCALCULATOROPTIONS_NMSALGORITHM,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=746,
)

_NONMAXSUPPRESSIONCALCULATOROPTIONS.fields_by_name['overlap_type'].enum_type = _NONMAXSUPPRESSIONCALCULATOROPTIONS_OVERLAPTYPE
_NONMAXSUPPRESSIONCALCULATOROPTIONS.fields_by_name['algorithm'].enum_type = _NONMAXSUPPRESSIONCALCULATOROPTIONS_NMSALGORITHM
_NONMAXSUPPRESSIONCALCULATOROPTIONS_OVERLAPTYPE.containing_type = _NONMAXSUPPRESSIONCALCULATOROPTIONS
_NONMAXSUPPRESSIONCALCULATOROPTIONS_NMSALGORITHM.containing_type = _NONMAXSUPPRESSIONCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['NonMaxSuppressionCalculatorOptions'] = _NONMAXSUPPRESSIONCALCULATOROPTIONS

NonMaxSuppressionCalculatorOptions = _reflection.GeneratedProtocolMessageType('NonMaxSuppressionCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _NONMAXSUPPRESSIONCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.util.non_max_suppression_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.NonMaxSuppressionCalculatorOptions)
  ))
_sym_db.RegisterMessage(NonMaxSuppressionCalculatorOptions)

_NONMAXSUPPRESSIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _NONMAXSUPPRESSIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_NONMAXSUPPRESSIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
