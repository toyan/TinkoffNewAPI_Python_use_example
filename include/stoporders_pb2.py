# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stoporders.proto
"""Generated protocol buffer code."""
import include.common_pb2 as common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='stoporders.proto',
    package='tinkoff.public.invest.api.contract.v1',
    syntax='proto3',
    serialized_options=b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\021Tinkoff/investAPI\242\002\005TIAPI\252\002\024Tinkoff.InvestAPI.V1\312\002\021Tinkoff\\Invest\\V1',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x10stoporders.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\xf8\x03\n\x14PostStopOrderRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nstop_price\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12L\n\tdirection\x18\x05 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.StopOrderDirection\x12\x12\n\naccount_id\x18\x06 \x01(\t\x12W\n\x0f\x65xpiration_type\x18\x07 \x01(\x0e\x32>.tinkoff.public.invest.api.contract.v1.StopOrderExpirationType\x12M\n\x0fstop_order_type\x18\x08 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.StopOrderType\x12/\n\x0b\x65xpire_date\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\".\n\x15PostStopOrderResponse\x12\x15\n\rstop_order_id\x18\x01 \x01(\t\"*\n\x14GetStopOrdersRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"^\n\x15GetStopOrdersResponse\x12\x45\n\x0bstop_orders\x18\x01 \x03(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.StopOrder\"C\n\x16\x43\x61ncelStopOrderRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x15\n\rstop_order_id\x18\x02 \x01(\t\"C\n\x17\x43\x61ncelStopOrderResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x92\x03\n\tStopOrder\x12\x15\n\rstop_order_id\x18\x01 \x01(\t\x12\x16\n\x0elots_requested\x18\x02 \x01(\x03\x12\x0c\n\x04\x66igi\x18\x03 \x01(\t\x12L\n\tdirection\x18\x04 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.StopOrderDirection\x12\x10\n\x08\x63urrency\x18\x05 \x01(\t\x12H\n\norder_type\x18\x06 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.StopOrderType\x12/\n\x0b\x63reate_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14\x61\x63tivation_date_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x65xpiration_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp*w\n\x12StopOrderDirection\x12$\n STOP_ORDER_DIRECTION_UNSPECIFIED\x10\x00\x12\x1c\n\x18STOP_ORDER_DIRECTION_BUY\x10\x01\x12\x1d\n\x19STOP_ORDER_DIRECTION_SELL\x10\x02*\xa5\x01\n\x17StopOrderExpirationType\x12*\n&STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED\x10\x00\x12/\n+STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL\x10\x01\x12-\n)STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE\x10\x02*\x90\x01\n\rStopOrderType\x12\x1f\n\x1bSTOP_ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bSTOP_ORDER_TYPE_TAKE_PROFIT\x10\x01\x12\x1d\n\x19STOP_ORDER_TYPE_STOP_LOSS\x10\x02\x12\x1e\n\x1aSTOP_ORDER_TYPE_STOP_LIMIT\x10\x03\x32\xc0\x03\n\x11StopOrdersService\x12\x8a\x01\n\rPostStopOrder\x12;.tinkoff.public.invest.api.contract.v1.PostStopOrderRequest\x1a<.tinkoff.public.invest.api.contract.v1.PostStopOrderResponse\x12\x8a\x01\n\rGetStopOrders\x12;.tinkoff.public.invest.api.contract.v1.GetStopOrdersRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetStopOrdersResponse\x12\x90\x01\n\x0f\x43\x61ncelStopOrder\x12=.tinkoff.public.invest.api.contract.v1.CancelStopOrderRequest\x1a>.tinkoff.public.invest.api.contract.v1.CancelStopOrderResponseBf\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x11Tinkoff/investAPI\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestAPI.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3',
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR, common__pb2.DESCRIPTOR, ])

_STOPORDERDIRECTION = _descriptor.EnumDescriptor(
    name='StopOrderDirection',
    full_name='tinkoff.public.invest.api.contract.v1.StopOrderDirection',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_DIRECTION_UNSPECIFIED', index=0, number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_DIRECTION_BUY', index=1, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_DIRECTION_SELL', index=2, number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1344,
    serialized_end=1463,
)
_sym_db.RegisterEnumDescriptor(_STOPORDERDIRECTION)

StopOrderDirection = enum_type_wrapper.EnumTypeWrapper(_STOPORDERDIRECTION)
_STOPORDEREXPIRATIONTYPE = _descriptor.EnumDescriptor(
    name='StopOrderExpirationType',
    full_name='tinkoff.public.invest.api.contract.v1.StopOrderExpirationType',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED', index=0, number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL', index=1, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE', index=2, number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1466,
    serialized_end=1631,
)
_sym_db.RegisterEnumDescriptor(_STOPORDEREXPIRATIONTYPE)

StopOrderExpirationType = enum_type_wrapper.EnumTypeWrapper(
    _STOPORDEREXPIRATIONTYPE)
_STOPORDERTYPE = _descriptor.EnumDescriptor(
    name='StopOrderType',
    full_name='tinkoff.public.invest.api.contract.v1.StopOrderType',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_TYPE_UNSPECIFIED', index=0, number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_TYPE_TAKE_PROFIT', index=1, number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_TYPE_STOP_LOSS', index=2, number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='STOP_ORDER_TYPE_STOP_LIMIT', index=3, number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1634,
    serialized_end=1778,
)
_sym_db.RegisterEnumDescriptor(_STOPORDERTYPE)

StopOrderType = enum_type_wrapper.EnumTypeWrapper(_STOPORDERTYPE)
STOP_ORDER_DIRECTION_UNSPECIFIED = 0
STOP_ORDER_DIRECTION_BUY = 1
STOP_ORDER_DIRECTION_SELL = 2
STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED = 0
STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL = 1
STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE = 2
STOP_ORDER_TYPE_UNSPECIFIED = 0
STOP_ORDER_TYPE_TAKE_PROFIT = 1
STOP_ORDER_TYPE_STOP_LOSS = 2
STOP_ORDER_TYPE_STOP_LIMIT = 3


_POSTSTOPORDERREQUEST = _descriptor.Descriptor(
    name='PostStopOrderRequest',
    full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='figi', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest.figi', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='quantity', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest.quantity', index=1,
            number=2, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='price', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest.price', index=2,
            number=3, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='stop_price', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest.stop_price', index=3,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='direction', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest.direction', index=4,
            number=5, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='account_id', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest.account_id', index=5,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='expiration_type', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest.expiration_type', index=6,
            number=7, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='stop_order_type', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest.stop_order_type', index=7,
            number=8, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='expire_date', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderRequest.expire_date', index=8,
            number=9, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=107,
    serialized_end=611,
)


_POSTSTOPORDERRESPONSE = _descriptor.Descriptor(
    name='PostStopOrderResponse',
    full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='stop_order_id', full_name='tinkoff.public.invest.api.contract.v1.PostStopOrderResponse.stop_order_id', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=613,
    serialized_end=659,
)


_GETSTOPORDERSREQUEST = _descriptor.Descriptor(
    name='GetStopOrdersRequest',
    full_name='tinkoff.public.invest.api.contract.v1.GetStopOrdersRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='account_id', full_name='tinkoff.public.invest.api.contract.v1.GetStopOrdersRequest.account_id', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=661,
    serialized_end=703,
)


_GETSTOPORDERSRESPONSE = _descriptor.Descriptor(
    name='GetStopOrdersResponse',
    full_name='tinkoff.public.invest.api.contract.v1.GetStopOrdersResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='stop_orders', full_name='tinkoff.public.invest.api.contract.v1.GetStopOrdersResponse.stop_orders', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=705,
    serialized_end=799,
)


_CANCELSTOPORDERREQUEST = _descriptor.Descriptor(
    name='CancelStopOrderRequest',
    full_name='tinkoff.public.invest.api.contract.v1.CancelStopOrderRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='account_id', full_name='tinkoff.public.invest.api.contract.v1.CancelStopOrderRequest.account_id', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='stop_order_id', full_name='tinkoff.public.invest.api.contract.v1.CancelStopOrderRequest.stop_order_id', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=801,
    serialized_end=868,
)


_CANCELSTOPORDERRESPONSE = _descriptor.Descriptor(
    name='CancelStopOrderResponse',
    full_name='tinkoff.public.invest.api.contract.v1.CancelStopOrderResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='time', full_name='tinkoff.public.invest.api.contract.v1.CancelStopOrderResponse.time', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=870,
    serialized_end=937,
)


_STOPORDER = _descriptor.Descriptor(
    name='StopOrder',
    full_name='tinkoff.public.invest.api.contract.v1.StopOrder',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='stop_order_id', full_name='tinkoff.public.invest.api.contract.v1.StopOrder.stop_order_id', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='lots_requested', full_name='tinkoff.public.invest.api.contract.v1.StopOrder.lots_requested', index=1,
            number=2, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='figi', full_name='tinkoff.public.invest.api.contract.v1.StopOrder.figi', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='direction', full_name='tinkoff.public.invest.api.contract.v1.StopOrder.direction', index=3,
            number=4, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='currency', full_name='tinkoff.public.invest.api.contract.v1.StopOrder.currency', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='order_type', full_name='tinkoff.public.invest.api.contract.v1.StopOrder.order_type', index=5,
            number=6, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='create_date', full_name='tinkoff.public.invest.api.contract.v1.StopOrder.create_date', index=6,
            number=7, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='activation_date_time', full_name='tinkoff.public.invest.api.contract.v1.StopOrder.activation_date_time', index=7,
            number=8, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='expiration_time', full_name='tinkoff.public.invest.api.contract.v1.StopOrder.expiration_time', index=8,
            number=9, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=940,
    serialized_end=1342,
)

_POSTSTOPORDERREQUEST.fields_by_name['price'].message_type = common__pb2._QUOTATION
_POSTSTOPORDERREQUEST.fields_by_name['stop_price'].message_type = common__pb2._QUOTATION
_POSTSTOPORDERREQUEST.fields_by_name['direction'].enum_type = _STOPORDERDIRECTION
_POSTSTOPORDERREQUEST.fields_by_name['expiration_type'].enum_type = _STOPORDEREXPIRATIONTYPE
_POSTSTOPORDERREQUEST.fields_by_name['stop_order_type'].enum_type = _STOPORDERTYPE
_POSTSTOPORDERREQUEST.fields_by_name['expire_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETSTOPORDERSRESPONSE.fields_by_name['stop_orders'].message_type = _STOPORDER
_CANCELSTOPORDERRESPONSE.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STOPORDER.fields_by_name['direction'].enum_type = _STOPORDERDIRECTION
_STOPORDER.fields_by_name['order_type'].enum_type = _STOPORDERTYPE
_STOPORDER.fields_by_name['create_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STOPORDER.fields_by_name['activation_date_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STOPORDER.fields_by_name['expiration_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['PostStopOrderRequest'] = _POSTSTOPORDERREQUEST
DESCRIPTOR.message_types_by_name['PostStopOrderResponse'] = _POSTSTOPORDERRESPONSE
DESCRIPTOR.message_types_by_name['GetStopOrdersRequest'] = _GETSTOPORDERSREQUEST
DESCRIPTOR.message_types_by_name['GetStopOrdersResponse'] = _GETSTOPORDERSRESPONSE
DESCRIPTOR.message_types_by_name['CancelStopOrderRequest'] = _CANCELSTOPORDERREQUEST
DESCRIPTOR.message_types_by_name['CancelStopOrderResponse'] = _CANCELSTOPORDERRESPONSE
DESCRIPTOR.message_types_by_name['StopOrder'] = _STOPORDER
DESCRIPTOR.enum_types_by_name['StopOrderDirection'] = _STOPORDERDIRECTION
DESCRIPTOR.enum_types_by_name['StopOrderExpirationType'] = _STOPORDEREXPIRATIONTYPE
DESCRIPTOR.enum_types_by_name['StopOrderType'] = _STOPORDERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostStopOrderRequest = _reflection.GeneratedProtocolMessageType('PostStopOrderRequest', (_message.Message,), {
    'DESCRIPTOR': _POSTSTOPORDERREQUEST,
    '__module__': 'stoporders_pb2'
    # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.PostStopOrderRequest)
})
_sym_db.RegisterMessage(PostStopOrderRequest)

PostStopOrderResponse = _reflection.GeneratedProtocolMessageType('PostStopOrderResponse', (_message.Message,), {
    'DESCRIPTOR': _POSTSTOPORDERRESPONSE,
    '__module__': 'stoporders_pb2'
    # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.PostStopOrderResponse)
})
_sym_db.RegisterMessage(PostStopOrderResponse)

GetStopOrdersRequest = _reflection.GeneratedProtocolMessageType('GetStopOrdersRequest', (_message.Message,), {
    'DESCRIPTOR': _GETSTOPORDERSREQUEST,
    '__module__': 'stoporders_pb2'
    # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetStopOrdersRequest)
})
_sym_db.RegisterMessage(GetStopOrdersRequest)

GetStopOrdersResponse = _reflection.GeneratedProtocolMessageType('GetStopOrdersResponse', (_message.Message,), {
    'DESCRIPTOR': _GETSTOPORDERSRESPONSE,
    '__module__': 'stoporders_pb2'
    # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetStopOrdersResponse)
})
_sym_db.RegisterMessage(GetStopOrdersResponse)

CancelStopOrderRequest = _reflection.GeneratedProtocolMessageType('CancelStopOrderRequest', (_message.Message,), {
    'DESCRIPTOR': _CANCELSTOPORDERREQUEST,
    '__module__': 'stoporders_pb2'
    # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CancelStopOrderRequest)
})
_sym_db.RegisterMessage(CancelStopOrderRequest)

CancelStopOrderResponse = _reflection.GeneratedProtocolMessageType('CancelStopOrderResponse', (_message.Message,), {
    'DESCRIPTOR': _CANCELSTOPORDERRESPONSE,
    '__module__': 'stoporders_pb2'
    # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.CancelStopOrderResponse)
})
_sym_db.RegisterMessage(CancelStopOrderResponse)

StopOrder = _reflection.GeneratedProtocolMessageType('StopOrder', (_message.Message,), {
    'DESCRIPTOR': _STOPORDER,
    '__module__': 'stoporders_pb2'
    # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.StopOrder)
})
_sym_db.RegisterMessage(StopOrder)


DESCRIPTOR._options = None

_STOPORDERSSERVICE = _descriptor.ServiceDescriptor(
    name='StopOrdersService',
    full_name='tinkoff.public.invest.api.contract.v1.StopOrdersService',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1781,
    serialized_end=2229,
    methods=[
        _descriptor.MethodDescriptor(
            name='PostStopOrder',
            full_name='tinkoff.public.invest.api.contract.v1.StopOrdersService.PostStopOrder',
            index=0,
            containing_service=None,
            input_type=_POSTSTOPORDERREQUEST,
            output_type=_POSTSTOPORDERRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='GetStopOrders',
            full_name='tinkoff.public.invest.api.contract.v1.StopOrdersService.GetStopOrders',
            index=1,
            containing_service=None,
            input_type=_GETSTOPORDERSREQUEST,
            output_type=_GETSTOPORDERSRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='CancelStopOrder',
            full_name='tinkoff.public.invest.api.contract.v1.StopOrdersService.CancelStopOrder',
            index=2,
            containing_service=None,
            input_type=_CANCELSTOPORDERREQUEST,
            output_type=_CANCELSTOPORDERRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_STOPORDERSSERVICE)

DESCRIPTOR.services_by_name['StopOrdersService'] = _STOPORDERSSERVICE

# @@protoc_insertion_point(module_scope)
