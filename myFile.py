import os

""" Class representing a File """
class myFile:
    # name = getName(self)? ...
    def __init__(self, path):
        self.path = path
        # self.name = name
        # self.size = size

    # ???
    def getSize(self):
        size = os.stat(self.name)
        print(size.st_size)

    # ???
    def getName(self):
        name = os.getcwd()
        print(name)
