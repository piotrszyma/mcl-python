import ctypes

from .. import hook

mclbn384_256 = hook.mclbls12_384


class Fr(ctypes.Structure):
    _fields_ = [("v", ctypes.c_ulonglong * 6)]

    def __init__(self, value=None):
        if value is None:
            return

        if isinstance(value, str):
            self.setStr(value)
        elif isinstance(value, int):
            self.setInt(value)

    def setInt(self, v):
        mclbn384_256.mclBnFr_setInt(ctypes.byref(self.v), v)

    def setStr(self, value: str):
        value = value if isinstance(value, bytes) else value.encode()
        error = mclbn384_256.mclBnFr_setStr(
            ctypes.byref(self.v), ctypes.c_char_p(value), len(value), 10
        )
        if error:
            raise RuntimeError("mclBnFr_setStr failed")

    def getStr(self):
        svLen = 2048
        sv = ctypes.create_string_buffer(b"\0" * svLen)
        mclbn384_256.mclBnFr_getStr(sv, svLen, ctypes.byref(self.v), 10)
        return sv.value.decode()

    def isZero(self):
        return mclbn384_256.mclBnFr_isZero(ctypes.byref(self.v)) != 0

    def isOne(self):
        return mclbn384_256.mclBnFr_isOne(ctypes.byref(self.v)) != 0

    def setByCSPRNG(self):
        return mclbn384_256.mclBnFr_setByCSPRNG(ctypes.byref(self.v))

    def __eq__(self, rhs):
        return (
            mclbn384_256.mclBnFr_isEqual(ctypes.byref(self.v), ctypes.byref(rhs.v)) != 0
        )

    def __ne__(self, rhs):
        return not (self == rhs)

    def __add__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnFr_add(
            ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v)
        )
        return ret

    def __sub__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnFr_sub(
            ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v)
        )
        return ret

    def __mul__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnFr_mul(
            ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v)
        )
        return ret

    def __div__(self, rhs):
        ret = Fr()
        mclbn384_256.mclBnFr_div(
            ctypes.byref(ret.v), ctypes.byref(self.v), ctypes.byref(rhs.v)
        )
        return ret

    def __invert__(self):
        ret = Fr()
        mclbn384_256.mclBnFr_neg(ctypes.byref(ret.v), ctypes.byref(self.v))
        return ret

    def __repr__(self):
        return f"Fr({self.getStr()})"
