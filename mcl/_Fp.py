import ctypes

from . import builder
from . import consts


class Fp(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * consts.FP_SIZE)]


Fp.setStr = builder.buildSetStr(Fp)
Fp.setInt = builder.buildSetInt(Fp)
Fp.setByCSPRNG = builder.buildSetByCSPRNG(Fp)
Fp.getStr = builder.buildGetStr(Fp)
Fp.isOne = builder.buildIsOne(Fp)
Fp.isZero = builder.buildIsZero(Fp)
Fp.__add__ = builder.buildThreeOp(Fp, "add")
Fp.__sub__ = builder.buildThreeOp(Fp, "sub")
Fp.__mul__ = builder.buildThreeOp(Fp, "mul")
Fp.__truediv__ = builder.buildThreeOp(Fp, "div")
Fp.__neg__ = builder.buildTwoOp(Fp, "neg")
Fp.__eq__ = builder.buildIsEqual(Fp)
