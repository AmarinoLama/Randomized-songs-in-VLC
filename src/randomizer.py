import random

def randomizer(array):

    # comprobamos si lo que introduce es una lista y si no se devuelve un mensaje

    try:
        assert isinstance(array,list)
    except AssertionError:
        print("No ha llegado a randomizer una lista de canciones")
        return None


    # si la lista tiene más de una canción se randomizará pero si no tiene más de una canción se devolverá un mensaje

    if len(array) > 1:
        random.shuffle(array)
        songsCorrect = [rf'{ruta}' for ruta in array]
        return songsCorrect
    
        # las canciones se devuelven en una lista con la respectiva ruta de cada una

    else:

        # si no hay canciones suficientes o no hay se devolverá un mensaje

        print("No hay caniones suficientes para mezclarlas")
        return None

if __name__ == "__main__":

    from searchSongs import searchSongs
    from findXSPF import findXSPF
    
    print(randomizer(["cancion1","cancion2","cancion3","cancion4","cancion5"]))
    assert randomizer(["cancion1","cancion2","cancion3","cancion4","cancion5"]) == ["cancion1","cancion2","cancion3","cancion4","cancion5"]
    assert randomizer(1) == None
    assert randomizer([]) == None

    print(randomizer(searchSongs(findXSPF())))