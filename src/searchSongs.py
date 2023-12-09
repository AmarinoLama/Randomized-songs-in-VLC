from findXSPF import findXSPF
import xml.etree.ElementTree as ET

def searchSongs():
    songs = []

    if findXSPF() is not None:
        tree = ET.parse(findXSPF())
        root = tree.getroot()

        for track in root.findall('.//{http://xspf.org/ns/0/}track'):
            locationElement = track.find('{http://xspf.org/ns/0/}location')
            if locationElement is not None and locationElement.text:
                songs.append(locationElement.text)

        return songs
    else:
        print("No se encontró el archivo XSPF, no se puede crear una lista de canciones.")
        return None
    
if __name__ == "__main__":

    print(findXSPF())
    print(searchSongs())