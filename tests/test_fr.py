import unittest

from mcl import Fr


def createRandomFr() -> Fr:
    fr = Fr()
    fr.setByCSPRNG()
    return fr


class FrTests(unittest.TestCase):
    @unittest.skip("Init args not yet supported")
    def testAdd(self):
        self.assertEqual(Fr(30), Fr(10) + Fr(20))

    @unittest.skip("Init args not yet supported")
    def testEquals(self):
        self.assertEqual(Fr(20), Fr(20))

    @unittest.skip("Init args not yet supported")
    def testInvert(self):
        self.assertEqual(Fr(10), ~~Fr(10))

    @unittest.skip("Init args not yet supported")
    def testMul(self):
        self.assertEqual(Fr(8), Fr(4) * Fr(2))

    @unittest.skip("Init args not yet supported")
    def testNeg(self):
        self.assertEqual(-Fr(10), Fr(8))

    def testInitFr(self):
        self.assertIsNotNone(Fr())

    def testSetStr(self):
        # Arrange.
        expected = b"12345678901234567"
        fr = Fr()

        # Act.
        fr.setStr(b"12345678901234567")

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

    def testMul(self):
        Fr() * Fr()

    def testGetStr(self):
        fr = Fr()
        fr.setStr(b"255")
        s = fr.getStr()
        self.assertEqual(b"255", s)

    def testByCSPRNG(self):
        Fr().setByCSPRNG()

    def testIsEqual(self):
        self.assertEqual(Fr(), Fr())
