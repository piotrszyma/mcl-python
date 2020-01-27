import unittest

from mcl import Fp


class FpTests(unittest.TestCase):
    def testInitFp(self):
        self.assertIsNotNone(Fp())

    def testSetByCSPRNG(self):
        Fp().setByCSPRNG()

    def testAdd(self):
        l = Fp()
        l.setInt(1)
        r = Fp()
        r.setInt(2)
        result = l + r
        self.assertEqual(result.getStr(), b"3")

    def testSub(self):
        Fp() - Fp()

    def testMul(self):
        Fp() * Fp()

    def testDiv(self):
        result = Fp() / Fp()

    def testNeg(self):
        not Fp()

    def testInv(self):
        base = Fp()
        base.setByCSPRNG()
        inv = ~base
        self.assertNotEqual(base, inv)
        inv_of_inv = ~inv
        self.assertEqual(base, inv_of_inv)

    def testSerialization(self):
        fp = Fp()
        fp.setByCSPRNG()
        serialized = fp.serialize()
        fp2 = Fp()
        fp2.deserialize(serialized)
        self.assertEqual(fp, fp2)

    def testStrRepr(self):
        fp = Fp()
        expected = "<class 'mcl.structures.Fp.Fp'> 0"
        self.assertEqual(expected, str(fp))

    @unittest.skip("setHashOf not yet implemented for FP")
    def testSetHashOf(self):
        pass

    @unittest.skip("mapToG1 not yet implemented for FP")
    def testMapToG1(self):
        pass

    def testStr(self):
        fp = Fp()
        fp.setStr(b"255")
        s = fp.getStr()
        self.assertEqual(b"255", s)

    def testSetInt(self):
        fp = Fp()
        fp.setInt(123)
        self.assertEqual(b"123", fp.getStr())

    def testIsZero(self):
        fp = Fp()
        fp.setInt(0)
        self.assertEqual(b"0", fp.getStr())
        self.assertTrue(fp.isZero())

    def testIsOne(self):
        fp = Fp()
        fp.setInt(1)
        self.assertEqual(b"1", fp.getStr())
        self.assertTrue(fp.isOne())

    def testRepr(self):
        fp = Fp()
        self.assertEqual(str(fp), repr(fp))
