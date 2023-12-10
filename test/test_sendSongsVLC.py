from src.sendSongsVLC import sendSongsVLC
from src.searchSongs import searchSongs
from src.findXSPF import findXSPF
from src.randomizer import randomizer

def test_songSended():
    assert (sendSongsVLC(randomizer(searchSongs(findXSPF())))) is True
    assert (sendSongsVLC(["cancion1", "cancion2"])) is True

def test_notSongs():
    assert (sendSongsVLC([])) is None
    assert (sendSongsVLC("hola")) is None