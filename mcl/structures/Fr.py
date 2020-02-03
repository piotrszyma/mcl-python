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
@class_binding()
class Fr(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * consts.FR_SIZE)]

    @classmethod
    @method_binding("mclBnFr_deserialize")
    def deserialize(cls, value: str) -> None:
        ...

    @method_binding("mclBnFr_getStr")
    def getStr(self, value: str) -> str:
        ...

    @method_binding("mclBnFr_isOne")
    def isOne(self) -> bool:
        ...

    @method_binding("mclBnFr_isZero")
    def isZero(self) -> bool:
        ...

    @method_binding("mclBnFr_serialize")
    def serialize(self) -> None:
        ...

    @method_binding("mclBnFr_setByCSPRNG")
    def setByCSPRNG(self) -> None:
        ...

    @method_binding("mclBnFr_setInt")
    def setInt(self, value: int) -> None:
        ...

    @method_binding("mclBnFr_setStr")
    def setStr(self, value: str) -> None:
        ...

    @method_binding("mclBnFr_add")
    def __add__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("mclBnFr_sub")
    def __sub__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("mclBnFr_div")
    def __truediv__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("mclBnFr_isEqual")
    def __eq__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("mclBnFr_inv")
    def __invert__(self) -> "Fr":
        ...

    @method_binding("mclBnFr_mul")
    def __mul__(self, other: "Fr") -> "Fr":
        ...

    @method_binding("mclBnFr_neg")
    def __neg__(self) -> "Fr":
        ...
