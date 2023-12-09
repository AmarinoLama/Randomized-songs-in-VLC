import xml.etree.ElementTree as ET

def searchSongs(locationXSPF):
    songs = []

    if locationXSPF is not None:
        tree = ET.parse(locationXSPF)
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

    from findXSPF import findXSPF

    print(searchSongs(findXSPF()))