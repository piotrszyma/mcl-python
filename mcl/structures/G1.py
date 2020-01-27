import types
import ctypes

from .. import utils
from .. import builder
from .Fp import Fp
from .Fr import Fr


@builder.provide_methods(
    builder.method('__add__').from_('add').using(builder.buildThreeOp),
    builder.method('__sub__').from_('sub').using(builder.buildThreeOp),
    builder.method('__neg__').from_('neg').using(builder.buildTwoOp),
    builder.method('__eq__').using(builder.buildIsEqual),
)
class G1(ctypes.Structure):
    _fields_ = [
        ("x", Fp),
        ("y", Fp),
        ("z", Fp),
    ]


G1.__mul__ = builder.buildMul(G1, Fr)
G1.deserialize = builder.buildDeserialize(G1)
G1.getStr = builder.buildGetStr(G1)
G1.hashAndMapTo = builder.buildHashAndMapTo(G1)
G1.isZero = builder.buildIsZero(G1)
G1.serialize = builder.buildSerialize(G1)
G1.setStr = builder.buildSetStr(G1)
