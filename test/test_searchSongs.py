from src.searchSongs import searchSongs
from src.findXSPF import findXSPF

def test_notFoundXSPF():
    assert searchSongs(None) == None

def test_existSongs():
    assert searchSongs(findXSPF()) is not None
    assert isinstance(searchSongs(findXSPF()), list)
    assert len(searchSongs(findXSPF())) > 1
    assert searchSongs(findXSPF()) is not []