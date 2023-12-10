import random

def randomizer(array):
    try:
        assert isinstance(array,list)
    except AssertionError:
        print("No ha llegado a randomizer una lista de canciones")
        return None

    if len(array) > 1:
        random.shuffle(array)
        songsCorrect = [rf'{ruta}' for ruta in array]
        return songsCorrect
    else:
        print("La lista de las canciones está vacía")
        return None

if __name__ == "__main__":

    from searchSongs import searchSongs
    from findXSPF import findXSPF
    
    print(randomizer(["cancion1","cancion2","cancion3","cancion4","cancion5"]))
    assert randomizer(["cancion1","cancion2","cancion3","cancion4","cancion5"]) == ["cancion1","cancion2","cancion3","cancion4","cancion5"]
    assert randomizer(1) == None
    assert randomizer([]) == None

    print(randomizer(searchSongs(findXSPF())))