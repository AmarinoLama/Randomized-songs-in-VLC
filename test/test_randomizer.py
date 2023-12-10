from src.randomizer import randomizer

def test_isShufled():
    assert randomizer(["cancion1","cancion2","cancion3","cancion4","cancion5"]) is not ["cancion1","cancion2","cancion3","cancion4","cancion5"]
    assert randomizer(["abc","asda","agig","hfudi","haoihf"]) is not ["abc","asda","agig","hfudi","haoihf"]

def test_isList():
    assert randomizer(1) == None
    assert randomizer('a') == None
    assert randomizer (["song1","song2"]) != None
    assert randomizer (None) == None

def test_isEmpty():
    assert randomizer([]) == None