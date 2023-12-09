from searchSongs import searchSongs
import random

def randomizer(array):
    
    try:
        assert isinstance(array,list)
    except AssertionError:
        print("No ha llegado a randomizer una lista de canciones")
        return None

    if array != []:
        listB = [x + 1 for x in range(len(array))]
        random.shuffle(listB)
        return dict(zip(array,listB))
    else:
        print("La lista de las canciones está vacía")
        return None

if __name__ == "__main__":

    #print(randomizer(["cancion1","cancion2","cancion3","cancion4","cancion5"]))
    #assert randomizer(["cancion1","cancion2","cancion3","cancion4","cancion5"]) != {'cancion1':1,'cancion2':2,'cancion3':3,'cancion4':4,'cancion5':5}
    #assert randomizer(1) == None
    #assert randomizer([]) == None
    print(randomizer(searchSongs()))