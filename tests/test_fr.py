import unittest

from mcl.wrapper.Fr import Fr

class FrTests(unittest.TestCase):
  
  def testInitFr(self):
    self.assertIsNotNone(Fr())

  def testSetStr(self):
    Fr().setStr(b"12345678901234567")

  def testSetInt(self):
    Fr().setInt(1)

  def testMul(self):
    Fr() * Fr()