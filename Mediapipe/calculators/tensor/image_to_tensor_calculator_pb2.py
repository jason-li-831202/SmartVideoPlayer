# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mediapipe/calculators/tensor/image_to_tensor_calculator.proto

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
  name='Mediapipe/calculators/tensor/image_to_tensor_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n=Mediapipe/calculators/tensor/image_to_tensor_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x1emediapipe/gpu/gpu_origin.proto\"\xa0\x06\n\x1eImageToTensorCalculatorOptions\x12\x1b\n\x13output_tensor_width\x18\x01 \x01(\x05\x12\x1c\n\x14output_tensor_height\x18\x02 \x01(\x05\x12\x19\n\x11keep_aspect_ratio\x18\x03 \x01(\x08\x12Y\n\x19output_tensor_float_range\x18\x04 \x01(\x0b\x32\x34.mediapipe.ImageToTensorCalculatorOptions.FloatRangeH\x00\x12U\n\x17output_tensor_int_range\x18\x07 \x01(\x0b\x32\x32.mediapipe.ImageToTensorCalculatorOptions.IntRangeH\x00\x12W\n\x18output_tensor_uint_range\x18\x08 \x01(\x0b\x32\x33.mediapipe.ImageToTensorCalculatorOptions.UIntRangeH\x00\x12-\n\ngpu_origin\x18\x05 \x01(\x0e\x32\x19.mediapipe.GpuOrigin.Mode\x12I\n\x0b\x62order_mode\x18\x06 \x01(\x0e\x32\x34.mediapipe.ImageToTensorCalculatorOptions.BorderMode\x1a&\n\nFloatRange\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\x1a$\n\x08IntRange\x12\x0b\n\x03min\x18\x01 \x01(\x03\x12\x0b\n\x03max\x18\x02 \x01(\x03\x1a%\n\tUIntRange\x12\x0b\n\x03min\x18\x01 \x01(\x04\x12\x0b\n\x03max\x18\x02 \x01(\x04\"K\n\nBorderMode\x12\x16\n\x12\x42ORDER_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x42ORDER_ZERO\x10\x01\x12\x14\n\x10\x42ORDER_REPLICATE\x10\x02\x32X\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xd3\xea\xb7\x9f\x01 \x01(\x0b\x32).mediapipe.ImageToTensorCalculatorOptionsB\x07\n\x05range')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_gpu_dot_gpu__origin__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE = _descriptor.EnumDescriptor(
  name='BorderMode',
  full_name='mediapipe.ImageToTensorCalculatorOptions.BorderMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BORDER_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BORDER_ZERO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BORDER_REPLICATE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=773,
  serialized_end=848,
)
_sym_db.RegisterEnumDescriptor(_IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE)


_IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE = _descriptor.Descriptor(
  name='FloatRange',
  full_name='mediapipe.ImageToTensorCalculatorOptions.FloatRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='mediapipe.ImageToTensorCalculatorOptions.FloatRange.min', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='mediapipe.ImageToTensorCalculatorOptions.FloatRange.max', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=656,
  serialized_end=694,
)

_IMAGETOTENSORCALCULATOROPTIONS_INTRANGE = _descriptor.Descriptor(
  name='IntRange',
  full_name='mediapipe.ImageToTensorCalculatorOptions.IntRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='mediapipe.ImageToTensorCalculatorOptions.IntRange.min', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='mediapipe.ImageToTensorCalculatorOptions.IntRange.max', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=732,
)

_IMAGETOTENSORCALCULATOROPTIONS_UINTRANGE = _descriptor.Descriptor(
  name='UIntRange',
  full_name='mediapipe.ImageToTensorCalculatorOptions.UIntRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='mediapipe.ImageToTensorCalculatorOptions.UIntRange.min', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max', full_name='mediapipe.ImageToTensorCalculatorOptions.UIntRange.max', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=734,
  serialized_end=771,
)

_IMAGETOTENSORCALCULATOROPTIONS = _descriptor.Descriptor(
  name='ImageToTensorCalculatorOptions',
  full_name='mediapipe.ImageToTensorCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_tensor_width', full_name='mediapipe.ImageToTensorCalculatorOptions.output_tensor_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_tensor_height', full_name='mediapipe.ImageToTensorCalculatorOptions.output_tensor_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keep_aspect_ratio', full_name='mediapipe.ImageToTensorCalculatorOptions.keep_aspect_ratio', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_tensor_float_range', full_name='mediapipe.ImageToTensorCalculatorOptions.output_tensor_float_range', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_tensor_int_range', full_name='mediapipe.ImageToTensorCalculatorOptions.output_tensor_int_range', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_tensor_uint_range', full_name='mediapipe.ImageToTensorCalculatorOptions.output_tensor_uint_range', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpu_origin', full_name='mediapipe.ImageToTensorCalculatorOptions.gpu_origin', index=6,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='border_mode', full_name='mediapipe.ImageToTensorCalculatorOptions.border_mode', index=7,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.ImageToTensorCalculatorOptions.ext', index=0,
      number=334361939, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[_IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE, _IMAGETOTENSORCALCULATOROPTIONS_INTRANGE, _IMAGETOTENSORCALCULATOROPTIONS_UINTRANGE, ],
  enum_types=[
    _IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='range', full_name='mediapipe.ImageToTensorCalculatorOptions.range',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=147,
  serialized_end=947,
)

_IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE.containing_type = _IMAGETOTENSORCALCULATOROPTIONS
_IMAGETOTENSORCALCULATOROPTIONS_INTRANGE.containing_type = _IMAGETOTENSORCALCULATOROPTIONS
_IMAGETOTENSORCALCULATOROPTIONS_UINTRANGE.containing_type = _IMAGETOTENSORCALCULATOROPTIONS
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_float_range'].message_type = _IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_int_range'].message_type = _IMAGETOTENSORCALCULATOROPTIONS_INTRANGE
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_uint_range'].message_type = _IMAGETOTENSORCALCULATOROPTIONS_UINTRANGE
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['gpu_origin'].enum_type = mediapipe_dot_gpu_dot_gpu__origin__pb2._GPUORIGIN_MODE
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['border_mode'].enum_type = _IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE
_IMAGETOTENSORCALCULATOROPTIONS_BORDERMODE.containing_type = _IMAGETOTENSORCALCULATOROPTIONS
_IMAGETOTENSORCALCULATOROPTIONS.oneofs_by_name['range'].fields.append(
  _IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_float_range'])
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_float_range'].containing_oneof = _IMAGETOTENSORCALCULATOROPTIONS.oneofs_by_name['range']
_IMAGETOTENSORCALCULATOROPTIONS.oneofs_by_name['range'].fields.append(
  _IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_int_range'])
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_int_range'].containing_oneof = _IMAGETOTENSORCALCULATOROPTIONS.oneofs_by_name['range']
_IMAGETOTENSORCALCULATOROPTIONS.oneofs_by_name['range'].fields.append(
  _IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_uint_range'])
_IMAGETOTENSORCALCULATOROPTIONS.fields_by_name['output_tensor_uint_range'].containing_oneof = _IMAGETOTENSORCALCULATOROPTIONS.oneofs_by_name['range']
DESCRIPTOR.message_types_by_name['ImageToTensorCalculatorOptions'] = _IMAGETOTENSORCALCULATOROPTIONS

ImageToTensorCalculatorOptions = _reflection.GeneratedProtocolMessageType('ImageToTensorCalculatorOptions', (_message.Message,), dict(

  FloatRange = _reflection.GeneratedProtocolMessageType('FloatRange', (_message.Message,), dict(
    DESCRIPTOR = _IMAGETOTENSORCALCULATOROPTIONS_FLOATRANGE,
    __module__ = 'mediapipe.calculators.tensor.image_to_tensor_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.ImageToTensorCalculatorOptions.FloatRange)
    ))
  ,

  IntRange = _reflection.GeneratedProtocolMessageType('IntRange', (_message.Message,), dict(
    DESCRIPTOR = _IMAGETOTENSORCALCULATOROPTIONS_INTRANGE,
    __module__ = 'mediapipe.calculators.tensor.image_to_tensor_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.ImageToTensorCalculatorOptions.IntRange)
    ))
  ,

  UIntRange = _reflection.GeneratedProtocolMessageType('UIntRange', (_message.Message,), dict(
    DESCRIPTOR = _IMAGETOTENSORCALCULATOROPTIONS_UINTRANGE,
    __module__ = 'mediapipe.calculators.tensor.image_to_tensor_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.ImageToTensorCalculatorOptions.UIntRange)
    ))
  ,
  DESCRIPTOR = _IMAGETOTENSORCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tensor.image_to_tensor_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ImageToTensorCalculatorOptions)
  ))
_sym_db.RegisterMessage(ImageToTensorCalculatorOptions)
_sym_db.RegisterMessage(ImageToTensorCalculatorOptions.FloatRange)
_sym_db.RegisterMessage(ImageToTensorCalculatorOptions.IntRange)
_sym_db.RegisterMessage(ImageToTensorCalculatorOptions.UIntRange)

_IMAGETOTENSORCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _IMAGETOTENSORCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_IMAGETOTENSORCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
