import unittest

from mcl import GT
from mcl import G2
from mcl import G1
from mcl import Fr

from . import test_data


class GTTests(unittest.TestCase):
    def testInitGT(self):
        self.assertIsNotNone(GT())

    def testPairing(self):
        fr1 = Fr()
        fr1.setByCSPRNG()

        g1 = G1()
        g1.setStr(test_data.G1_STR)

        g2 = G2()
        g2.setStr(test_data.G2_STR)

        fr2 = Fr()
        fr2.setByCSPRNG()

        gt = GT.pairing(g1 * fr1, g2 * fr2)

        self.assertIsNotNone(gt)
