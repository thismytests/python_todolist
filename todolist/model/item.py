import math
import time


class Item:
    __title = ''
    __status = False
    __id = None

    def __init__(self):
        # todo... will be refactoring here
        self.__id =  math.ceil(time.time())

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def status(self):
        return self.__status

    def setItemSelected(self):
        self.__status = True

    def setItemUnSelected(self):
        self.__status = False

if __name__ == '__main__':
    print('eee')