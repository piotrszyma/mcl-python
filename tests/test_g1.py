import unittest

from mcl.wrapper.G1 import G1

class G1Tests(unittest.TestCase):
  
  def testInitG1(self):
    self.assertIsNotNone(G1())

  def testSetGetStr(self):
    expected_s = b"1 3685416753713387016781088315183077757961620795782546409894578378688607592378376318836054947676345821548104185464507 1339506544944476473020471379941921221584933875938349620426543736416511423956333506472724655353366534992391756441569"
    g1 = G1()
    g1.setStr(expected_s)
    s = g1.getStr()
    self.assertEqual(expected_s, s)

  def testOperations(self):
    G1() * G1()
    G1() + G1()
    G1() - G1()
    not G1()
