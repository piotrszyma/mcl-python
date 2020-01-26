import ctypes

from . import utils
from .Fp import Fp
from .hook import mclbn384_256

class G1(ctypes.Structure):
    _fields_ = [
      ("x", Fp),
      ("y", Fp),
      ("z", Fp),
    ]

    def setStr(self, s, mode=10):
        mclBnG1_setStr = utils.wrap_function(mclbn384_256, 'mclBnG1_setStr', None, [ctypes.POINTER(G1), ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int64])
        ret = mclBnG1_setStr(self, ctypes.c_char_p(s), len(s), mode)
        if ret:
            raise RuntimeError(ret)

    def getStr(self, mode=10):
        svLen = 2048
        sv = ctypes.create_string_buffer(b"\0" * svLen)
        mclBnG1_getStr = utils.wrap_function(mclbn384_256, 'mclBnG1_getStr', None, [(ctypes.c_char * (svLen + 1)), ctypes.c_int64, ctypes.POINTER(G1), ctypes.c_size_t])
        ret = mclBnG1_getStr(sv, svLen, self, 10)
        if ret:
            print("ERR Fr:getStr")
        return sv.value

    def __str__(self):
        return self.getStr()

    def isZero(self):
        mclBnG1_isZero = utils.wrap_function(mclbn384_256, 'mclBnG1_isZero', ctypes.c_int64, [ctypes.POINTER(G1)])
        return mclbn384_256.mclBnG1_isZero(self) != 0

    def isOne(self):
        mclBnG1_isOne = utils.wrap_function(mclbn384_256, 'mclBnG1_isOne', ctypes.c_int64, [ctypes.POINTER(G1)])
        return mclbn384_256.mclBnG1_isOne(self.v) != 0

    def __eq__(self, other):
        mclBnG1_isEqual = utils.wrap_function(mclbn384_256, 'mclBnG1_isEqual', ctypes.c_int64, [ctypes.POINTER(G1), ctypes.POINTER(G1)])
        return mclbn384_256.mclBnG1_isEqual(self, other) != 0

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        result = G1()
        mclBnG1_add = utils.wrap_function(mclbn384_256, 'mclBnG1_add', None, [ctypes.POINTER(G1), ctypes.POINTER(G1), ctypes.POINTER(G1)])
        mclBnG1_add(result, self, other)
        return result

    def __sub__(self, other):
        result = G1()
        mclBnG1_sub = utils.wrap_function(mclbn384_256, 'mclBnG1_sub', None, [ctypes.POINTER(G1), ctypes.POINTER(G1), ctypes.POINTER(G1)])
        mclBnG1_sub(result, self, other)
        return result

    def __mul__(self, other):
        result = G1()
        mclBnG1_mul = utils.wrap_function(mclbn384_256, 'mclBnG1_mul', None, [ctypes.POINTER(G1), ctypes.POINTER(G1), ctypes.POINTER(G1)])
        mclBnG1_mul(result, self, other)
        return result

    def __neg__(self):
        result = G1()
        mclbn384_256.mclBnG1_neg(result, self)
        return result

