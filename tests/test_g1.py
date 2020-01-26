import unittest

from mcl import G1
from mcl import Fr

G1_POINT = b"1 3685416753713387016781088315183077757961620795782546409894578378688607592378376318836054947676345821548104185464507 1339506544944476473020471379941921221584933875938349620426543736416511423956333506472724655353366534992391756441569"


class G1Tests(unittest.TestCase):
    def testInitG1(self):
        self.assertIsNotNone(G1())

    def testSetGetStr(self):
        g1 = G1()
        g1.setStr(G1_POINT)
        s = g1.getStr()
        self.assertEqual(G1_POINT, s)

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
        g1.setStr(G1_POINT)

        random_fr = Fr()
        random_fr.setByCSPRNG()

        random_fr2 = Fr()
        random_fr2.setByCSPRNG()
        self.assertNotEqual(g1 * random_fr, g1 * random_fr2)

    def testHashAndMapTo(self):
        g1 = G1.hashAndMapTo(b"test")
