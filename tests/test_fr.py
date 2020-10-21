import unittest

from mcl import Fr


def createRandomFr() -> Fr:
    fr = Fr()
    fr.setByCSPRNG()
    return fr


class FrTests(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(Fr(30), Fr(10) + Fr(20))

    def testEquals(self):
        self.assertEqual(Fr(20), Fr(20))

    def testInvert(self):
        self.assertEqual(Fr(10), ~~Fr(10))

    def testMul(self):
        self.assertEqual(Fr(8), Fr(4) * Fr(2))

    def testInitFr(self):
        self.assertIsNotNone(Fr())

    def testSetStr(self):
        # Arrange.
        expected = "1234567"
        fr = Fr()

        # Act.
        fr.setStr("1234567")

        # Assert.
        self.assertEqual(expected, fr.getStr())

    def testIsEqual(self):
        # Arrange.
        fr = createRandomFr()

        fr2 = Fr()
        fr2.setStr(fr.getStr())

        self.assertEqual(fr, fr2)

    def testSetInt(self):
        Fr().setInt(1)

    def testGetStr(self):
        fr = Fr()
        fr.setStr("255")
        s = fr.getStr()
        self.assertEqual("255", s)

    def testByCSPRNG(self):
        Fr().setByCSPRNG()

