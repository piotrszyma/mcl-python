import ctypes

from . import utils
from .Fp2 import Fp2
from .hook import mclbn384_256

class G2(ctypes.Structure):
    _fields_ = [
      ("x", Fp2),
      ("y", Fp2),
      ("z", Fp2),
    ]

    def setStr(self, s, mode=10):
        mclBnG2_setStr = utils.wrap_function(mclbn384_256, 'mclBnG2_setStr', None, [ctypes.POINTER(G2), ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int64])
        ret = mclBnG2_setStr(self, ctypes.c_char_p(s), len(s), mode)
        if ret:
            raise RuntimeError(ret)

    def getStr(self, mode=10):
        svLen = 2048
        sv = ctypes.create_string_buffer(b"\0" * svLen)
        mclBnG2_getStr = utils.wrap_function(mclbn384_256, 'mclBnG2_getStr', None, [(ctypes.c_char * (svLen + 1)), ctypes.c_int64, ctypes.POINTER(G2), ctypes.c_size_t])
        ret = mclBnG2_getStr(sv, svLen, self, mode)
        if ret:
            print("ERR Fr:getStr")
        return sv.value

    def __str__(self):
        return self.getStr()

    def isZero(self):
        mclBnG2_isZero = utils.wrap_function(mclbn384_256, 'mclBnG2_isZero', ctypes.c_int64, [ctypes.POINTER(G2)])
        return mclbn384_256.mclBnG2_isZero(self) != 0

    def isOne(self):
        mclBnG2_isOne = utils.wrap_function(mclbn384_256, 'mclBnG2_isOne', ctypes.c_int64, [ctypes.POINTER(G2)])
        return mclbn384_256.mclBnG2_isOne(self.v) != 0

    def __eq__(self, other):
        mclBnG2_isEqual = utils.wrap_function(mclbn384_256, 'mclBnG2_isEqual', ctypes.c_int64, [ctypes.POINTER(G2), ctypes.POINTER(G2)])
        return mclbn384_256.mclBnG2_isEqual(self, other) != 0

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        result = G2()
        mclBnG2_add = utils.wrap_function(mclbn384_256, 'mclBnG2_add', None, [ctypes.POINTER(G2), ctypes.POINTER(G2), ctypes.POINTER(G2)])
        mclBnG2_add(result, self, other)
        return result

    def __sub__(self, other):
        result = G2()
        mclBnG2_sub = utils.wrap_function(mclbn384_256, 'mclBnG2_sub', None, [ctypes.POINTER(G2), ctypes.POINTER(G2), ctypes.POINTER(G2)])
        mclBnG2_sub(result, self, other)
        return result

    def __mul__(self, other):
        result = G2()
        mclBnG2_mul = utils.wrap_function(mclbn384_256, 'mclBnG2_mul', None, [ctypes.POINTER(G2), ctypes.POINTER(G2), ctypes.POINTER(G2)])
        mclBnG2_mul(result, self, other)
        return result

    def __neg__(self):
        result = G2()
        mclbn384_256.mclBnG2_neg(result, self)
        return result

