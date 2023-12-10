from src.searchSongs import searchSongs
from src.findXSPF import findXSPF

def test_notFoundXSPF():
    assert searchSongs(None) == None

def test_existSongs():
    assert searchSongs(findXSPF()) is not None
    assert isinstance(searchSongs(findXSPF()), list)
    assert len(searchSongs(findXSPF())) > 1
    assert searchSongs(findXSPF()) is not []

# caso test para cuando el archivo xspf no tiene canciones, es decir la localización en el xspf está vacía (caso particular, si se hace este otros fallarán)

def test_noSongs():
    assert (searchSongs(findXSPF())) == None