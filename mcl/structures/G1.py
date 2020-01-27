from .. import utils
from .. import builder
from . import base

from .Fp import Fp
from .Fr import Fr


@builder.provide_methods(
    builder.method("__add__").using(builder.buildThreeOp).with_args("add"),
    builder.method("__eq__").using(builder.buildIsEqual),
    builder.method("__mul__").using(builder.buildMul).with_args(Fr),
    builder.method("__neg__").using(builder.buildTwoOp).with_args("neg"),
    builder.method("__sub__").using(builder.buildThreeOp).with_args("sub"),
    builder.method("deserialize"),
    builder.method("getStr"),
    builder.method("hashAndMapTo"),
    builder.method("isZero"),
    builder.method("serialize"),
    builder.method("setStr"),
)
class G1(base.Structure):
    _fields_ = [
        ("x", Fp),
        ("y", Fp),
        ("z", Fp),
    ]
