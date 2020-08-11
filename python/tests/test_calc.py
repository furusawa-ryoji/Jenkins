import unittest
import calc


class TestCalc(unittest.TestCase):
    
    # @classmethod
    # def setUpClass(self):
    #     print("set up class")
    
    # def setUp(self):
    #     print("set up")
    
    def test_plus_s01(self):
        self.assertEqual(calc.plus(1, 2), 3)
        
    def test_plus_s02(self):
        self.assertEqual(calc.plus(1, 3), 4)
        
    def test_minus_s03(self):
        self.assertEqual(calc.minus(1, 3), -2)
        
    def test_minus_s04(self):
        self.assertEqual(calc.minus(999, 3), 996)
    
    def test_minus_s05(self):
        pass

    # def tearDown(self):
    #     print("tear down")
    
    # @classmethod
    # def tearDownClass(self):
    #     print("tear down class")