import ctypes

from .Fp import Fp
from ..hook import mclbls12_384


class Fp2(ctypes.Structure):
    _fields_ = [("d", Fp * 2)]
