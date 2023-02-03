# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mediapipe/calculators/tensor/tensors_to_segmentation_calculator.proto

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
from Mediapipe.gpu import gpu_origin_pb2 as mediapipe_dot_gpu_dot_gpu__origin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Mediapipe/calculators/tensor/tensors_to_segmentation_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\nEMediapipe/calculators/tensor/tensors_to_segmentation_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x1emediapipe/gpu/gpu_origin.proto\"\xe2\x02\n&TensorsToSegmentationCalculatorOptions\x12-\n\ngpu_origin\x18\x01 \x01(\x0e\x32\x19.mediapipe.GpuOrigin.Mode\x12V\n\nactivation\x18\x02 \x01(\x0e\x32<.mediapipe.TensorsToSegmentationCalculatorOptions.Activation:\x04NONE\x12\x1d\n\x12output_layer_index\x18\x03 \x01(\x05:\x01\x31\"0\n\nActivation\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07SIGMOID\x10\x01\x12\x0b\n\x07SOFTMAX\x10\x02\x32`\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xc2\x91\xbe\xb2\x01 \x01(\x0b\x32\x31.mediapipe.TensorsToSegmentationCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_gpu_dot_gpu__origin__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TENSORSTOSEGMENTATIONCALCULATOROPTIONS_ACTIVATION = _descriptor.EnumDescriptor(
  name='Activation',
  full_name='mediapipe.TensorsToSegmentationCalculatorOptions.Activation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGMOID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFTMAX', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=363,
  serialized_end=411,
)
_sym_db.RegisterEnumDescriptor(_TENSORSTOSEGMENTATIONCALCULATOROPTIONS_ACTIVATION)


_TENSORSTOSEGMENTATIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TensorsToSegmentationCalculatorOptions',
  full_name='mediapipe.TensorsToSegmentationCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gpu_origin', full_name='mediapipe.TensorsToSegmentationCalculatorOptions.gpu_origin', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activation', full_name='mediapipe.TensorsToSegmentationCalculatorOptions.activation', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_layer_index', full_name='mediapipe.TensorsToSegmentationCalculatorOptions.output_layer_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TensorsToSegmentationCalculatorOptions.ext', index=0,
      number=374311106, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
    _TENSORSTOSEGMENTATIONCALCULATOROPTIONS_ACTIVATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=509,
)

_TENSORSTOSEGMENTATIONCALCULATOROPTIONS.fields_by_name['gpu_origin'].enum_type = mediapipe_dot_gpu_dot_gpu__origin__pb2._GPUORIGIN_MODE
_TENSORSTOSEGMENTATIONCALCULATOROPTIONS.fields_by_name['activation'].enum_type = _TENSORSTOSEGMENTATIONCALCULATOROPTIONS_ACTIVATION
_TENSORSTOSEGMENTATIONCALCULATOROPTIONS_ACTIVATION.containing_type = _TENSORSTOSEGMENTATIONCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['TensorsToSegmentationCalculatorOptions'] = _TENSORSTOSEGMENTATIONCALCULATOROPTIONS

TensorsToSegmentationCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorsToSegmentationCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _TENSORSTOSEGMENTATIONCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tensor.tensors_to_segmentation_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TensorsToSegmentationCalculatorOptions)
  ))
_sym_db.RegisterMessage(TensorsToSegmentationCalculatorOptions)

_TENSORSTOSEGMENTATIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TENSORSTOSEGMENTATIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORSTOSEGMENTATIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
