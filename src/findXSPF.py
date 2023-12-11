import os

def findXSPF():

    # en primer lugar busca si el xspf está en la misma carpeta del proyecto

    filesInDirectory = os.listdir(os.getcwd())
    correctFile = [file for file in filesInDirectory if file.endswith('xspf')]
    userName = os.getenv('USERNAME')

    if len(correctFile) == 0:

        # en segundo lugar se busca si el xspf está en la carpeta de música

        ruta_music = r'C:\\Users\\' + userName + r'\\Music'
        filesInDirectory = os.listdir(ruta_music)
        correctFile = [file for file in filesInDirectory if file.endswith('xspf')]
        if len(correctFile) == 0:

            # si el xspf no está en ningún lugar de los mencionados anteriormente se devuelve un mensaje

            print("No se encontró el xspf")
            return None
        elif len(correctFile) >= 1:
            return ruta_music + r"\\" + correctFile[0]
    elif len(correctFile) >= 1:
        return r"C:\\Users\\"+ userName + r"\\Desktop\\proyectoVLC\\Randomized-songs-in-VLC\\" + correctFile[0]
    
# en ambos return (si se encuentra el xspf) se devolverá la ruta exacta del xspf

if __name__ == "__main__":

    print(findXSPF())
    assert findXSPF().startswith(r"C:\\")
    assert findXSPF().endswith(".xspf")
    assert isinstance(findXSPF(), str)