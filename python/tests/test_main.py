import unittest
import main

import enum
import pathlib
from datetime import datetime

class TestCalc(unittest.TestCase):
    # @classmethod
    # def setUpClass(self):
    #     print("set up class")
        
    def test_login_s01(self):
        self.assertEqual(main.title1,'ポータル')
    
    def test_login_s02(self):
        self.assertEqual(main.title2,'ログイン - サイボウズ Office')
    
    def test_login_s03(self):
        self.assertEqual(main.title3,'トップページ - サイボウズ Office')
    
    # @classmethod
    # def tearDownClass(self):
    #     print("tear down class")
        
def _main():
    """The main process at script execution."""
    @enum.unique
    class Verbosity(enum.IntEnum):
        NOTHING = 0
        SIMPLE = 1
        DETAIL = 2

    CURRENT_PATH = pathlib.Path('result.txt')
    EXEC_DATETIME = datetime.today()
    FILE_MOD_DATETIME = datetime.fromtimestamp(CURRENT_PATH.stat().st_mtime)
    LOG_PATH = CURRENT_PATH.with_name(
        CURRENT_PATH.stem + f'_{EXEC_DATETIME.date()}.log')

    with open(pathlib.Path(LOG_PATH), 'w') as fw:
        fw.write(
            f'[Date of script modification] {str(FILE_MOD_DATETIME)}\n'
            f'[Date of this test execution] {str(EXEC_DATETIME)}\n'
            '\n')

        unittest.main(
            testRunner=unittest.TextTestRunner(
                stream=fw,
                descriptions=False,
                verbosity=Verbosity.DETAIL))


if __name__ == '__main__':
    _main()