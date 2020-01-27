import ctypes

from .. import builder
from .. import consts
from . import base


@builder.provide_methods(
    builder.method("__add__").using(builder.buildThreeOp).with_args("add"),
    builder.method("__eq__").using(builder.buildIsEqual),
    builder.method("__invert__").using(builder.buildTwoOp).with_args("inv"),
    builder.method("__mul__").using(builder.buildThreeOp).with_args("mul"),
    builder.method("__neg__").using(builder.buildTwoOp).with_args("neg"),
    builder.method("__sub__").using(builder.buildThreeOp).with_args("sub"),
    builder.method("__truediv__").using(builder.buildThreeOp).with_args("div"),
    builder.method("deserialize"),
    builder.method("getStr"),
    builder.method("isOne"),
    builder.method("isZero"),
    builder.method("serialize"),
    builder.method("setByCSPRNG"),
    builder.method("setInt"),
    builder.method("setStr"),
)
class Fp(base.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * consts.FP_SIZE)]
