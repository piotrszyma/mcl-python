import ctypes
import os 
import pathlib
import os
import contextlib

DIR_FOR_LINKER = pathlib.Path(__file__).parent.absolute()

MCLBN384_256 = 5

@contextlib.contextmanager
def change_cwd(path):
  current_cwd = os.getcwd()
  os.chdir(path)
  try:
    yield
  finally:
    os.chdir(current_cwd)


with change_cwd(DIR_FOR_LINKER):
  mclbn384_256 = ctypes.CDLL('lib/libmclbn384_256.dylib')

ret = mclbn384_256.mclBn_init(MCLBN384_256, 46)

if ret:
  raise RuntimeError(f"mclbn384_256 ret {ret}")