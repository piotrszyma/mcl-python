import ctypes

from .hook import mclbn384_256
from .Fp import Fp


class Fp2(ctypes.Structure):
    _fields_ = [("d", Fp * 2)]
