from src.sendSongsVLC import sendSongsVLC
from src.searchSongs import searchSongs
from src.findXSPF import findXSPF
from src.randomizer import randomizer

if __name__ == "__main__":

    sendSongsVLC(randomizer(searchSongs(findXSPF())))