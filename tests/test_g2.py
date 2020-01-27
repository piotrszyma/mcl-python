import unittest

from mcl import G2
from mcl import Fr

from . import test_data


class G2Tests(unittest.TestCase):
    def testInitG2(self):
        self.assertIsNotNone(G2())

    def testSetGetStr(self):
        g2 = G2()
        g2.setStr(test_data.G2_STR)
        s = g2.getStr()
        self.assertEqual(test_data.G2_STR, s)

    def testAdd(self):
        G2() + G2()

    def testSub(self):
        G2() - G2()

    def testMul(self):
        G2() * Fr()

    def testNeg(self):
        not G2()

    def testHashAndMapTo(self):
        g1 = G2.hashAndMapTo(b"test")
