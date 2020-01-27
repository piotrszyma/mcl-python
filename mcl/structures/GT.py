from .. import utils
from .. import builder
from . import base
from .G1 import G1
from .G2 import G2
from .Fp import Fp


@builder.provide_methods(
    builder.method("__invert__").using(builder.buildTwoOp).with_args("inv"),
    builder.method("pairing").using(builder.buildPairing).with_args(G1, G2),
)
class GT(base.Structure):
    _fields_ = [
        ("d", (Fp * 12)),
    ]
