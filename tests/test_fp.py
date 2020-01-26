
import unittest

from mcl.wrapper.Fp import Fp

class FpTests(unittest.TestCase):
  
  def testInitFp(self):
    self.assertIsNotNone(Fp())

  def testGetStr(self):
    fp = Fp()
    fp.setStr(b'255')
    s = fp.getStr()
    self.assertEqual(255, s[0])

  def testSetInt(self):
    Fp().setInt(1)

  def testByCSPRNG(self):
    res = Fp().setByCSPRNG()
    self.assertEqual(0, res)