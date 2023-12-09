import os

# el xspf esta dentro de la carpeta musica
# el xspf esta dentro del proyecto

def findXSPF():

    filesInDirectory = os.listdir(os.getcwd())
    correctFile = [file for file in filesInDirectory if file.endswith('xspf')]

    if len(correctFile) == 0:
        userName = os.getenv('USERNAME')
        ruta_music = r'C:\\Users\\' + userName + r'\\Music'
        filesInDirectory = os.listdir(ruta_music)
        correctFile = [file for file in filesInDirectory if file.endswith('xspf')]
        if len(correctFile) == 0:
            return "No se encontró el xspf"
        elif len(correctFile) == 1:
            return correctFile
        elif len(correctFile) > 1:
            return correctFile[0]
    elif len(correctFile) == 1:
        return correctFile
    elif len(correctFile) > 1:
        return correctFile[0]

print(findXSPF())