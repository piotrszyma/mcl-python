import types
import ctypes

from .. import utils
from .. import builder
from .Fp import Fp
from .Fr import Fr


@builder.provide_methods(
    builder.method('__add__').using(builder.buildThreeOp).with_args('add'),
    builder.method('__eq__').using(builder.buildIsEqual),
    builder.method('__mul__').using(builder.buildMul).with_args(Fr),
    builder.method('__neg__').using(builder.buildTwoOp).with_args('neg'),
    builder.method('__sub__').using(builder.buildThreeOp).with_args('sub'),
    builder.method('deserialize').using(builder.buildDeserialize),
    builder.method('getStr').using(builder.buildGetStr),
    builder.method('hashAndMapTo').using(builder.buildHashAndMapTo),
    builder.method('isZero').using(builder.buildIsZero),
    builder.method('serialize').using(builder.buildSerialize),
    builder.method('setStr').using(builder.buildSetStr),
)
class G1(ctypes.Structure):
    _fields_ = [
        ("x", Fp),
        ("y", Fp),
        ("z", Fp),
    ]
