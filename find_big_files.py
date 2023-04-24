import os
import glob
from myFile import myFile

largeFiles = []
sortedFilesList = []
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
    path = input("Enter a folder path: ")
    
    # default path for testing purposes
    path = 'C:/Users/Jonas/Pictures/Wallpaper/**/*.png'
    found_file_paths = getFilesList(path)
    print(found_file_paths)
    
    filesList = []
    for path in found_file_paths:
        # print(type(path))
        f = myFile(path)
        filesList.append(f)

    print(filesList[:3])
