import os
import shutil
import time

def gatherFileExtensionsFromDirectory(dir):
    extensions = []
    for fileName in os.listdir(dir):
        fileExt = fileName[fileName.rfind("."): ]
        if fileExt not in extensions:
            extensions.append(fileExt)
    return extensions

def examineFilesInDirectory(dir, list):
    relevantFiles = []
    for fileName in os.listdir(dir):
        for fileExt in list:
            if fileExt in fileName:
                relevantFiles.append(fileName)
    return relevantFiles

def checkIfFileAlreadyExistsInDirectory(dir, list):
    toAdd = []
    checkAgainst = os.listdir(dir)
    for file in list:
        if file not in checkAgainst:
            toAdd.append(file)
    return toAdd

def moveFilesToDirectory(list, srcLoc, destLoc):
    for file in list:
        shutil.move(srcLoc+"/"+file, destLoc)


def main():
    coolStuff = "C:\\Users\\Lucas\\Desktop\\coolStuff"
    downloads = "C:\\Users\\Lucas\\Downloads"

    extensions = gatherFileExtensionsFromDirectory(coolStuff)
    while True:
        relevantFiles = examineFilesInDirectory(downloads, extensions)
        toAdd = checkIfFileAlreadyExistsInDirectory(coolStuff, relevantFiles)
        moveFilesToDirectory(toAdd, downloads, coolStuff)
        time.sleep(60)

main()
