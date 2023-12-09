from findXSPF import findXSPF
import xml.etree.ElementTree as ET

def searchSongs():
    songs = []
    if findXSPF() is not None:
        tree = ET.parse(''.join(map(str, findXSPF())))
        root = tree.getroot()
        for child in root.findall('.//tracklist/track/location'):
            print(child)
            location = child.text
            songs.append(location)
        return tree
    else:
        print("No se encontró el XSPF por lo que no se puede crear una lista de canciones")
        return None
    
if __name__ == "__main__":

    print(searchSongs())

    #C:\Users\Nitiriotan\Desktop\proyectoVLC\Randomized-songs-in-VLC