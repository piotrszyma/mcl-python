import ctypes

from .hook import mclbn384_256


class G1(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * 4)]

    def setInt(self, v):
        mclbn384_256.mclBnG1_setInt(self.v, v)

    def setStr(self, s):
        ret = mclbn384_256.mclBnG1_setStr(self.v, ctypes.c_char_p(s), len(s), 10)
        print(ret)
        if ret:
            print("ERR Fr:setStr")

    def __str__(self):
        svLen = 1024
        sv = ctypes.create_string_buffer("\0" * svLen)
        ret = mclbn384_256.mclBnG1_getStr(sv, svLen, self.v)
        if ret:
            print("ERR Fr:getStr")
        return sv.value

    def isZero(self):
        return mclbn384_256.mclBnG1_isZero(self.v) != 0

    def isOne(self):
        return mclbn384_256.mclBnG1_isOne(self.v) != 0

    def __eq__(self, rhs):
        return mclbn384_256.mclBnG1_isEqual(self.v, rhs.v) != 0

    def __ne__(self, rhs):
        return not (P == Q)

    def __add__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnG1_add(ret.v, self.v, rhs.v)
        return ret

    def __sub__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnG1_sub(ret.v, self.v, rhs.v)
        return ret

    def __mul__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnG1_mul(ret.v, self.v, rhs.v)
        return ret

    def __div__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnG1_div(ret.v, self.v, rhs.v)
        return ret

    def __neg__(self):
        ret = Fr()
        mclbn384_256.mclBnG1_neg(ret.v, self.v)
        return ret

