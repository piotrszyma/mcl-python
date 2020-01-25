import ctypes

from .hook import mclbn384_256


class Fr(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * 4)]

    def setInt(self, v):
        mclbn384_256.mclBnFr_setInt(self.v, v)

    def setStr(self, s):
        ret = mclbn384_256.mclBnFr_setStr(self.v, ctypes.c_char_p(s), len(s), 10)
        if ret:
            print("ERR Fr:setStr")

    def __str__(self):
        svLen = 1024
        sv = ctypes.create_string_buffer("\0" * svLen)
        ret = mclbn384_256.mclBnFr_getStr(sv, svLen, self.v)
        if ret:
            print("ERR Fr:getStr")
        return sv.value

    def isZero(self):
        return mclbn384_256.mclBnFr_isZero(self.v) != 0

    def isOne(self):
        return mclbn384_256.mclBnFr_isOne(self.v) != 0

    def __eq__(self, rhs):
        return mclbn384_256.mclBnFr_isEqual(self.v, rhs.v) != 0

    def __ne__(self, rhs):
        return not (P == Q)

    def __add__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnFr_add(ret.v, self.v, rhs.v)
        return ret

    def __sub__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnFr_sub(ret.v, self.v, rhs.v)
        return ret

    def __mul__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnFr_mul(ret.v, self.v, rhs.v)
        return ret

    def __div__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnFr_div(ret.v, self.v, rhs.v)
        return ret

    def __neg__(self):
        ret = Fr()
        mclbn384_256.mclBnFr_neg(ret.v, self.v)
        return ret

