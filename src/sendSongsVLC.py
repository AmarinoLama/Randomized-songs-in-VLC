import subprocess

def sendSongsVLC(array):

    if isinstance(array, list) != True:
        return None
    
    if len(array) >= 1:
        print("Ha funcionado")
        subprocess.run([r"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"]+array, shell=True)
        return True
    else:
        print("No se ha encontrado ninguna canción")
        return None
    
if __name__ == "__main__":
    from searchSongs import searchSongs
    from findXSPF import findXSPF
    from randomizer import randomizer
    
    print(sendSongsVLC(randomizer(searchSongs(findXSPF()))))