import unittest
import main

class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("set up class")
        
    def test_login_s01(self):
        self.assertEqual(main.title1,'ポータル')
    
    def test_login_s02(self):
        self.assertEqual(main.title2,'ログイン - サイボウズ Office')
    
    def test_login_s03(self):
        self.assertEqual(main.title3,'トップページ - サイボウズ Office')
    
    @classmethod
    def tearDownClass(self):
        print("tear down class")
        
if __name__ == '__main__':
    unittest.main()