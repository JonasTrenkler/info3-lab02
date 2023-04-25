import os
import glob
# from myFile import myFile

class myFile:
    # name = getName(self)? ...
    def __init__(self, path):
        self.path = path
        # self.name = name
        # self.size = size


    # ???
    def getSize(self):
        size = os.path.getsize(self.path)
        print(size/ (1024*1024))
        return (size/ (1024*1024))

# largeFiles = []
# sortedFilesList = []
# path = 'C:/Users/estel/OneDrive/Bilder/Screenshots**/*.png' #path example

def getFilesList(path):
    return glob.glob(path, recursive=True)
    # files = glob.glob(path, recursive=True)
    # for file in files:
    #     # files.append(file)
    #     filesList.append(file)
    #     # print(file)

# def sortFilesList():
#     for file in found_file_paths:
#         if file.size >= 10.0:
#             largeFiles.append(file)
#             print(largeFiles)
#         else:
#             sortedFilesList.append(file)
#             print(sortedFilesList)

if __name__ == "__main__":
    # path = input("Enter a folder path: ")

    largeFiles = []
    sortedFilesList = []
    
    # default path for testing purposes
    path = 'C:/Users/estel/OneDrive/Bilder/Screenshots**/*.png'
    found_file_paths = getFilesList(path)
    # print(found_file_paths)
    
    filesList = []
    for path in found_file_paths:
        # print(type(path))
        f = myFile(path)
        filesList.append(f)

    print(filesList[:3])

    for file in filesList:
        if file.getSize() >= 0.3:
            largeFiles.append(file)
            # print(largeFiles)
        else:
            sortedFilesList.append(file)
            # print(sortedFilesList)

    print('The files', largeFiles, 'is too big')
