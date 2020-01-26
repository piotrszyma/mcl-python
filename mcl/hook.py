import contextlib
import ctypes
import os
import pathlib
import platform

from . import consts

DIR_FOR_LINKER = os.environ.get("MCL_PATH", "/usr/local/lib/libmcl")


@contextlib.contextmanager
def change_cwd(path):
    current_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_cwd)


with change_cwd(DIR_FOR_LINKER):
    system = platform.system()
    if system == 'Darwin':
        mclbn384_256 = ctypes.CDLL("lib/libmclbn384_256.dylib")
    elif system == 'Linux':
        mclbn384_256 = ctypes.CDLL("lib/libmclbn384_256.so")
    else:
        raise RuntimeError(f"Unsupported OS {system}")


ret = mclbn384_256.mclBn_init(consts.BN384_256, consts.MCLBN_COMPILED_TIME_VAR)

if ret:
    raise RuntimeError(f"mclbn384_256 ret {ret}")
