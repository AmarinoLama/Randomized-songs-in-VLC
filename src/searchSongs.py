import xml.etree.ElementTree as ET

def searchSongs(locationXSPF):

    # si no se introduce un None se ejecutará el localizador de canciones

    if locationXSPF is not None:
        songs = []
        tree = ET.parse(locationXSPF)
        root = tree.getroot()

        # se busca en el xspf las rutas de las canciones y se guardan en una lista

        for track in root.findall('.//{http://xspf.org/ns/0/}track'):
            locationElement = track.find('{http://xspf.org/ns/0/}location')
            if locationElement is not None and locationElement.text:
                songs.append(locationElement.text)

        if len(songs) >= 1:

            # si hay una o más canciones se devolverá la lista de ellas

            return songs
        else:

            # si hay cero canciones en la lista significa que no se han encontrado canciones por lo que se devolverá un mensaje

            print("No hay canciones dentro del XSPF")
            return None
    else:

        # si se introduce None devolverá un mensaje

        print("No se encontró el archivo XSPF, no se puede crear una lista de canciones.")
        return None
    
if __name__ == "__main__":

    from findXSPF import findXSPF

    print(searchSongs(findXSPF()))

    assert searchSongs(findXSPF()) is not None
    assert isinstance(searchSongs(findXSPF()), list)
    assert len(searchSongs(findXSPF())) > 1