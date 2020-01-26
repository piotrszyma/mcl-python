import ctypes

from . import builder
from . import consts


class Fr(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * consts.FR_SIZE)]


Fr.setStr = builder.buildSetStr(Fr)
Fr.setInt = builder.buildSetInt(Fr)
Fr.setByCSPRNG = builder.buildSetByCSPRNG(Fr)
Fr.getStr = builder.buildGetStr(Fr)
Fr.isOne = builder.buildIsOne(Fr)
Fr.isZero = builder.buildIsZero(Fr)
Fr.__add__ = builder.buildThreeOp(Fr, "add")
Fr.__sub__ = builder.buildThreeOp(Fr, "sub")
Fr.__mul__ = builder.buildThreeOp(Fr, "mul")
Fr.__truediv__ = builder.buildThreeOp(Fr, "div")
Fr.__neg__ = builder.buildTwoOp(Fr, "neg")
Fr.__eq__ = builder.buildIsEqual(Fr)
