from src.randomizer import randomizer

def test_isShufled():
    assert randomizer(["cancion1","cancion2","cancion3","cancion4","cancion5"]) != {'cancion1':1,'cancion2':2,'cancion3':3,'cancion4':4,'cancion5':5}
    assert randomizer(["abc","asda","agig","hfudi","haoihf"]) != {"abc":1,"asda":2,"agig":3,"hfudi":4,"haoihf":5}

def test_isList():
    assert randomizer(1) == None
    assert randomizer('a') == None
    assert randomizer (["song1","song2"]) != None
    assert randomizer (None) == None

def test_isEmpty():
    assert randomizer([]) == None