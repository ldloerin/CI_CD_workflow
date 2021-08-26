import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])

class PathAppend():
    def statement():
        my_path = os.path.split(os.path.dirname(__file__))[0]
        print('Added ' + my_path + ' to sys.path')
