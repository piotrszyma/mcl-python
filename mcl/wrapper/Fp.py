import ctypes

from . import utils
from .hook import mclbn384_256

class Fp(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * 6)]

    def setInt(self, value: int) -> None:
        mclBnFp_setInt = utils.wrap_function(mclbn384_256, 'mclBnFp_setInt', None, [ctypes.POINTER(Fp), ctypes.c_int64])
        mclBnFp_setInt(self, value)

    def setStr(self, s, mode=10):
        mclBnFp_setStr = utils.wrap_function(mclbn384_256, 'mclBnFp_setStr', None, [ctypes.POINTER(Fp), ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int64])
        return mclBnFp_setStr(self, ctypes.c_char_p(s), len(s), mode)

    def setByCSPRNG(self):
        mclBnFp_setByCSPRNG = utils.wrap_function(mclbn384_256, 'mclBnFp_setByCSPRNG', ctypes.c_int64, [ctypes.POINTER(Fp)])
        return mclBnFp_setByCSPRNG(self)

    def getStr(self):
        svLen = 2048
        sv = ctypes.create_string_buffer(b"\0" * svLen)
        mclbn384_256.mclBnFp_getStr(sv, svLen, self.v)
        return sv.value
