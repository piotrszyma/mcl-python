import types
import ctypes

from . import utils
from . import builder
from ._G1 import G1
from ._G2 import G2
from ._Fp import Fp

BUFFER_SIZE = 2048


class GT(ctypes.Structure):
    _fields_ = [
        ("d", (Fp * 12)),
    ]


GT.__invert__ = builder.buildTwoOp(GT, "inv")
GT.pairing = builder.buildPairing(GT, G1, G2)
