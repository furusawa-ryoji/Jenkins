import unittest
import enum
from pathlib import Path
from datetime import datetime
import logging

def _main():
    """The main process at script execution."""
    @enum.unique
    class Verbosity(enum.IntEnum):
        NOTHING = 0
        SIMPLE = 1
        DETAIL = 2

    CURRENT_PATH = Path('./file/report.txt')
    EXEC_DATETIME = datetime.today()
    FILE_MOD_DATETIME = datetime.fromtimestamp(CURRENT_PATH.stat().st_mtime)
    LOG_PATH = CURRENT_PATH.with_name(
        CURRENT_PATH.stem + f'_{EXEC_DATETIME.date()}.log')
    
    with open(CURRENT_PATH, mode='w') as fw:
        fw.write(
            f'[Date of script modification] {str(FILE_MOD_DATETIME)}\n'
            f'[Date of this test execution] {str(EXEC_DATETIME)}\n'
            '\n')

        unittest.main(
            module="tests.test_login", 
            testRunner=unittest.TextTestRunner(
                stream=fw,
                descriptions=False,
                verbosity=Verbosity.DETAIL))


if __name__ == '__main__':
    _main()