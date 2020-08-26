import os
import sys
from pathlib import Path
sys.path.append(os.path.abspath("file"))

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)
CURRENT_PATH = os.path.abspath('file\\result.txt')
print(CURRENT_PATH)
