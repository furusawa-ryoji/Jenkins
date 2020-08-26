print(__name__)

import login
import unittest

class TestCalc(unittest.TestCase):
    # @classmethod
    # def setUpClass(self):
    #     print("set up class")
    
    def login(self):
        pass
        
        
    def test_login_s01(self):
        self.assertEqual(login.title1, 'ポータル')
    
    def test_login_s02(self):
        self.assertEqual(login.title2,'ログイン - サイボウズ Office')
    
    def test_login_s03(self):
        self.assertEqual(login.title3,'トップページ - サイボウズ Office')
    
    # @classmethod
    # def tearDownClass(self):
    #     print("tear down class")
