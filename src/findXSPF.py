import os

# el xspf esta dentro de la carpeta musica
# el xspf esta dentro del proyecto

def findXSPF():

    filesInDirectory = os.listdir(os.getcwd())
    correctFile = [file for file in filesInDirectory if file.endswith('xspf')]
    userName = os.getenv('USERNAME')

    if len(correctFile) == 0:
        ruta_music = r'C:\\Users\\' + userName + r'\\Music'
        filesInDirectory = os.listdir(ruta_music)
        correctFile = [file for file in filesInDirectory if file.endswith('xspf')]
        if len(correctFile) == 0:
            print("No se encontró el xspf")
            return None
        elif len(correctFile) >= 1:
            return ruta_music + correctFile[0]
    elif len(correctFile) >= 1:
        return r"C:\\Users\\"+ userName + r"\\Desktop\\proyectoVLC\\Randomized-songs-in-VLC\\" + correctFile[0]

if __name__ == "__main__":

    print(findXSPF())