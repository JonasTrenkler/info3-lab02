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
        size = os.stat(self.path)
        print(size.st_size/ (1024*1024))

    # filesList = []
    # largeFiles = []
    # sortedFilesList = []

    # ???
""" def getName(self):
        name = os.getcwd()
        print(name)"""
