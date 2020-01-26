import ctypes

from .Fp import Fp
from ..hook import mclbn384_256


class Fp2(ctypes.Structure):
    _fields_ = [("d", Fp * 2)]
