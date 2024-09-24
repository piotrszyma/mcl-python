import ctypes
import dataclasses
import inspect

from . import hook
from . import utils

BUFFER_SIZE = 2048


def tryGetBuilderMethodFromGlobals(method_name: str) -> callable:
    return globals().get("build" + method_name[0].upper() + method_name[1:])


class WrappedMethodDefinition:
    def __init__(self, as_method):
        self.as_method = as_method
        self.from_method = as_method
        self.builder_method = tryGetBuilderMethodFromGlobals(self.as_method)
        self.args = []

    def using(self, builder_method):
        self.builder_method = builder_method
        return self

    def with_args(self, *args):
        self.args = args
        return self

    def apply(self, cls):
        method = self.builder_method(cls, *self.args)
        setattr(cls, self.as_method, method)


def method(as_method):
    return WrappedMethodDefinition(as_method)


def provide_methods(*definitions):
    def decorator(cls):

        for definition in definitions:
            definition.apply(cls)

        return cls

    return decorator


def buildSetStr(cls):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_setStr",
        [ctypes.POINTER(cls), ctypes.c_char_p, ctypes.c_size_t, ctypes.c_int64],
    )

    def setStr(self, value, mode=10):
        return wrapper(self, value, len(value), mode)

    return setStr


def buildSetInt(cls):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_setInt",
        [ctypes.POINTER(cls), ctypes.c_int64],
    )

    def setInt(self, value):
        return wrapper(self, value)

    return setInt


def buildSetByCSPRNG(cls):
    wrapper = utils.wrap_function(
        hook.mclbls12_384, f"mclBn{cls.__name__}_setByCSPRNG", [ctypes.POINTER(cls)],
    )

    def setByCSPRNG(self):
        return wrapper(self)

    return setByCSPRNG


def buildGetStr(cls):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_getStr",
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
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_isEqual",
        [ctypes.POINTER(cls), ctypes.POINTER(cls)],
        ctypes.c_int64,
    )

    def isEqual(self, other):
        return wrapper(self, other) == 1

    return isEqual


def buildIsOne(cls):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_isOne",
        [ctypes.POINTER(cls)],
        ctypes.c_int64,
    )

    def isOne(self):
        return wrapper(self) == 1

    return isOne


def buildIsZero(cls):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_isZero",
        [ctypes.POINTER(cls)],
        ctypes.c_int64,
    )

    def isZero(self):
        return wrapper(self) == 1

    return isZero


def buildThreeOp(cls, op_name):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_{op_name}",
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
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_{op_name}",
        [ctypes.POINTER(cls), ctypes.POINTER(cls)],
    )

    def op(self):
        result = cls()
        wrapper(result, self)
        return result

    op.__name__ = op_name
    return op


def buildMul(cls, right_op):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_mul",
        [ctypes.POINTER(cls), ctypes.POINTER(cls), ctypes.POINTER(right_op)],
    )

    def mul(self, right):
        result = cls()
        wrapper(result, self, right)
        return result

    return mul


def buildSerialize(cls):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_serialize",
        [
            (ctypes.c_char * (BUFFER_SIZE + 1)),
            ctypes.c_size_t,
            ctypes.POINTER(cls),
            ctypes.c_uint64,
        ],
    )

    def serialize(self, mode=10):
        buffer = ctypes.create_string_buffer(b"\0" * BUFFER_SIZE)
        length = wrapper(buffer, BUFFER_SIZE, self, mode)
        return buffer.raw[:length]

    return serialize


def buildDeserialize(cls):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_deserialize",
        [ctypes.POINTER(cls), ctypes.c_char_p, ctypes.c_size_t],
    )

    def deserialize(self, value):
        wrapper(self, value, len(value))

    return deserialize


def buildHashAndMapTo(cls):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn{cls.__name__}_hashAndMapTo",
        [ctypes.POINTER(cls), ctypes.c_char_p, ctypes.c_size_t],
    )

    @staticmethod
    def hashAndMapTo(value):
        result = cls()
        wrapper(result, ctypes.c_char_p(value), len(value))
        return result

    return hashAndMapTo


def buildPairing(cls, left_group, right_group):
    wrapper = utils.wrap_function(
        hook.mclbls12_384,
        f"mclBn_pairing",
        (ctypes.POINTER(cls), ctypes.POINTER(left_group), ctypes.POINTER(right_group)),
    )

    @staticmethod
    def pairing(g1, g2):
        result = cls()
        wrapper(result, g1, g2)
        return result

    return pairing
