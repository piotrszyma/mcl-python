import ctypes

from . import hook
from . import utils

BUFFER_SIZE = 2048


def buildSetStr(cls):
    wrapper = utils.wrap_function(
        hook.mclbn384_256,
        f"mclBn{cls.__name__}_setStr",
        None,
        [ctypes.POINTER(cls), ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int64],
    )

    def setStr(self, value, mode=10):
        return wrapper(self, value, len(value), mode)

    return setStr


def buildSetInt(cls):
    wrapper = utils.wrap_function(
        hook.mclbn384_256,
        f"mclBn{cls.__name__}_setInt",
        None,
        [ctypes.POINTER(cls), ctypes.c_int64],
    )

    def setInt(self, value):
        return wrapper(self, value)

    return setInt


def buildSetByCSPRNG(cls):
    wrapper = utils.wrap_function(
        hook.mclbn384_256,
        f"mclBn{cls.__name__}_setByCSPRNG",
        None,
        [ctypes.POINTER(cls)],
    )

    def setByCSPRNG(self):
        return wrapper(self)

    return setByCSPRNG


def buildGetStr(cls):
    wrapper = utils.wrap_function(
        hook.mclbn384_256,
        f"mclBn{cls.__name__}_getStr",
        None,
        [
            (ctypes.c_char * (BUFFER_SIZE + 1)),
            ctypes.c_size_t,
            ctypes.POINTER(cls),
            ctypes.c_uint64,
        ],
    )

    def getStr(self, mode=10):
        buffer = ctypes.create_string_buffer(b"\0" * BUFFER_SIZE)
        wrapper(buffer, BUFFER_SIZE, self, mode)
        return buffer.value

    return getStr


def buildIsEqual(cls):
    wrapper = utils.wrap_function(
        hook.mclbn384_256,
        f"mclBnFp_isEqual",
        None,
        [ctypes.POINTER(cls), ctypes.POINTER(cls)],
    )

    def isEqual(self, other):
        return wrapper(self, other) != 0

    return isEqual


def buildIsOne(cls):
    wrapper = utils.wrap_function(
        hook.mclbn384_256, f"mclBnFp_isOne", None, [ctypes.POINTER(cls)],
    )

    def isOne(self, other):
        return wrapper(self) != 0

    return isOne


def buildIsZero(cls):
    wrapper = utils.wrap_function(
        hook.mclbn384_256, f"mclBnFp_isZero", None, [ctypes.POINTER(cls)],
    )

    def isZero(self, other):
        return wrapper(self) != 0

    return isZero


def buildThreeOp(cls, op_name):
    wrapper = utils.wrap_function(
        hook.mclbn384_256,
        f"mclBnFp_{op_name}",
        None,
        [ctypes.POINTER(cls), ctypes.POINTER(cls), ctypes.POINTER(cls)],
    )

    def op(self, other):
        result = cls()
        wrapper(result, self, other)
        return result

    op.__name__ = op_name
    return op


def buildTwoOp(cls, op_name):
    wrapper = utils.wrap_function(
        hook.mclbn384_256,
        f"mclBnFp_{op_name}",
        None,
        [ctypes.POINTER(cls), ctypes.POINTER(cls)],
    )

    def op(self):
        result = cls()
        wrapper(result, self)
        return result

    op.__name__ = op_name
    return op
