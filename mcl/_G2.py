import types
import ctypes

from . import utils
from . import builder
from ._Fp2 import Fp2

BUFFER_SIZE = 2048


class G2(ctypes.Structure):
    _fields_ = [
        ("x", Fp2),
        ("y", Fp2),
        ("z", Fp2),
    ]

    def setStr(self, s, mode=10):
        return mclBnG2.setStr(self, ctypes.c_char_p(s), len(s), mode)

    def getStr(self, mode=10):
        buffer = ctypes.create_string_buffer(b"\0" * BUFFER_SIZE)
        mclBnG2.getStr(buffer, BUFFER_SIZE, self, 10)
        return buffer.value

    def __str__(self):
        return self.getStr()

    def isZero(self):
        return mclBnG2.isZero(self) != 0

    def __eq__(self, other):
        return mclBnG2.isEqual(self, other) != 0

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        result = G2()
        mclBnG2.add(result, self, other)
        return result

    def __sub__(self, other):
        result = G2()
        mclBnG2.sub(result, self, other)
        return result

    def __mul__(self, other):
        result = G2()
        mclBnG2.mul(result, self, other)
        return result

    def __neg__(self):
        result = G2()
        mclBnG2.neg(result, self)
        return result


G2.setStr = builder.buildSetStr(G2)
G2.getStr = builder.buildGetStr(G2)
G2.isZero = builder.buildIsZero(G2)
G2.__add__ = builder.buildThreeOp(G2, "add")
G2.__sub__ = builder.buildThreeOp(G2, "sub")
G2.__mul__ = builder.buildThreeOp(G2, "mul")
G2.__neg__ = builder.buildTwoOp(G2, "neg")
G2.__eq__ = builder.buildIsEqual(G2)
