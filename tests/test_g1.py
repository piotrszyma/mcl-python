import unittest

from mcl.wrapper import G1

class G1Tests(unittest.TestCase):
  
  def testInitFr(self):
    self.assertIsNotNone(G1())

  # def testSetStr(self):
  #   Fr().setStr(b"12345678901234567")

  # def testSetInt(self):
  #   Fr().setInt(1)

  # def testMul(self):
  #   Fr() * Fr()