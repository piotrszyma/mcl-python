import functools


def wrap_function(lib, funcname, argtypes, restype=None):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func
