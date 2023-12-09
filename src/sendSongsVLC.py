from randomizer import randomizer
from searchSongs import searchSongs
import subprocess

def sendSongsVLC():
    if len(searchSongs()) > 1:
        print("Ha funcionado")
        subprocess.run("cd C:\Program Files\VideoLAN\VLC", shell=True)
    else:
        print("No se ha encontrado ninguna canción")
        return None
    
print(sendSongsVLC())