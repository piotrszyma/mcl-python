import ctypes

from .. import builder
from .. import consts

from mcl.bindings import class_binding
from mcl.bindings import method_binding


# @builder.provide_methods(
#     builder.method("__add__").using(builder.buildThreeOp).with_args("add"),
#     builder.method("__eq__").using(builder.buildIsEqual),
#     builder.method("__invert__").using(builder.buildTwoOp).with_args("inv"),
#     builder.method("__mul__").using(builder.buildThreeOp).with_args("mul"),
#     builder.method("__neg__").using(builder.buildTwoOp).with_args("neg"),
#     builder.method("__sub__").using(builder.buildThreeOp).with_args("sub"),
#     builder.method("__truediv__").using(builder.buildThreeOp).with_args("div"),
#     builder.method("deserialize"),
#     builder.method("getStr"),
#     builder.method("isOne"),
#     builder.method("isZero"),
#     builder.method("serialize"),
#     builder.method("setByCSPRNG"),
#     builder.method("setInt"),
#     builder.method("setStr"),
# )
@class_binding("mclBnFr")
class Fr(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * consts.FR_SIZE)]

    @classmethod
    @method_binding("deserialize")
    def deserialize(cls, value: str) -> None:
        ...

    @method_binding("getStr")
    def getStr(self, value: str) -> str:
        ...

    @method_binding("isOne")
    def isOne(self) -> bool:
        ...

    @method_binding("isZero")
    def isZero(self) -> bool:
        ...

    @method_binding("serialize")
    def serialize(self) -> None:
        ...

    @method_binding("setByCSPRNG")
    def setByCSPRNG(self) -> None:
        ...

    @method_binding("setInt")
    def setInt(self, value: int) -> None:
        ...

    @method_binding("setStr")
    def setStr(self, value: str) -> None:
        ...

    @method_binding("add")
    def __add__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("sub")
    def __sub__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("div")
    def __truediv__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("isEqual")
    def __eq__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("inv")
    def __invert__(self) -> "Fr":
        ...

    @method_binding("mul")
    def __mul__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("mul")
    def __neg__(self) -> "Fr":
        ...
