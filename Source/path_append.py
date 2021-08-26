import os
import sys
sys.path.append(os.path.split(os.path.dirname(__file__))[0])


class PathAppend():
    def __init__(self):
        self.my_path = os.path.split(os.path.dirname(__file__))[0]
        self.__statement()

    def __statement(self):
        print('Added ' + self.my_path + ' to sys.path')
