import unittest

from mcl import G1
from mcl import Fr

from . import test_data


class G1Tests(unittest.TestCase):
    def testInitG1(self):
        self.assertIsNotNone(G1())

    def testSetGetStr(self):
        g1 = G1()
        g1.setStr(test_data.G1_STR)
        s = g1.getStr()
        self.assertEqual(test_data.G1_STR, s)

    def testEqual(self):
        e1 = G1()
        e1.setStr(test_data.G1_STR)
        e2 = G1()
        e2.setStr(test_data.G1_STR)
        self.assertTrue(e1 == e2)

    def testAdd(self):
        G1() + G1()

    def testSub(self):
        G1() - G1()

    def testMul(self):
        G1() * Fr()

    def testNeg(self):
        not G1()

    def testNeq(self):
        g1 = G1()
        g1.setStr(test_data.G1_STR)

        random_fr = Fr()
        random_fr.setByCSPRNG()

        random_fr2 = Fr()
        random_fr2.setByCSPRNG()
        self.assertNotEqual(g1 * random_fr, g1 * random_fr2)

    def testHashAndMapTo(self):
        g1 = G1.hashAndMapTo(b"test")
