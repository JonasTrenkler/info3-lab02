import os
import glob


class File:
    # name = getName(self)? ...
    def __init__(self, name, size, path):
        self.name = name
        self.size = size
        self.path = path

    # ???
    def getSize(self):
        size = os.stat(self.name)
        print(size.st_size)

    # ???
    def getName(self):
        name = os.getcwd()
        print(name)

# alles ab hier in seperate class/main?
    filesList = []
    largeFiles = []
    sortedFilesList = []
    path = 'C:/Users/estel/OneDrive/Bilder/Screenshots**/*.png' #path example

    def printFilesList(self):
        files = glob.glob(self.path,
                          recursive=True)
            for file in files:
                # files.append(file)
                filesList.append(file)
                # print(file)

        print(filesList)


    def sortFilesList(self):
        for file in filesList:
            if file.size >= 10.0:
                largeFiles.append(file)
                print(largeFiles)
            else:
                sortedFilesList.append(file)
                print(sortedFilesList)
