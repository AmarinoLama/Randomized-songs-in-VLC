import subprocess

def sendSongsVLC(array):

    # si llega algo distinto a una lista se devolverá un mensaje

    if isinstance(array, list) != True:
        print("No ha llegado una lista")
        return None
    
    # Si llega una lista de canciones se mandará al VLC

    if len(array) >= 1:

        # Se ejecuta el comando

        subprocess.run([r"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"] + array, shell=True)

        # Se devuelve un mensaje conforme a funcionado todo correctamente

        return "Ha funcionado"
    else:

        # Si dentro de la lista no hay ninguna canción se devolverá un mensaje

        print("No se ha encontrado ninguna canción")
        return None
    
if __name__ == "__main__":
    from searchSongs import searchSongs
    from findXSPF import findXSPF
    from randomizer import randomizer
    
    print(sendSongsVLC(randomizer(searchSongs(findXSPF()))))