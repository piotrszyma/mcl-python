import ctypes

from .. import builder
from .. import consts

@builder.provide_methods(
    builder.method('__add__').using(builder.buildThreeOp).with_args('add'),
    builder.method('__eq__').using(builder.buildIsEqual),
    builder.method('__invert__').using(builder.buildTwoOp).with_args('inv'),
    builder.method('__mul__').using(builder.buildThreeOp).with_args('mul'),
    builder.method('__neg__').using(builder.buildTwoOp).with_args('neg'),
    builder.method('__sub__').using(builder.buildThreeOp).with_args('sub'),
    builder.method('__truediv__').using(builder.buildThreeOp).with_args('div'),
    builder.method('deserialize').using(builder.buildDeserialize),
    builder.method('getStr').using(builder.buildGetStr),
    builder.method('isOne').using(builder.buildIsOne),
    builder.method('isZero').using(builder.buildIsZero),
    builder.method('serialize').using(builder.buildSerialize),
    builder.method('setByCSPRNG').using(builder.buildSetByCSPRNG),
    builder.method('setInt').using(builder.buildSetInt),
    builder.method('setStr').using(builder.buildSetStr),
)
class Fr(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * consts.FR_SIZE)]
