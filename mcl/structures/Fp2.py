from .Fp import Fp
from ..hook import mclbls12_384
from . import base


class Fp2(base.Structure):
    _fields_ = [("d", Fp * 2)]
