import os

def findXml():
    filesInDirectory = os.listdir(os.getcwd())
    correctFile = [file for file in filesInDirectory if file.endswith('xspf')]
    finalFile = correctFile
    return finalFile

print(findXml())
print(os.getcwd())