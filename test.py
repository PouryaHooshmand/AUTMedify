import shutil
import sys

try:
    shutil.move(src='/home/milad/test2/test.txt', dst='/home/milad/')
except IOError as Error:
    print(Error)