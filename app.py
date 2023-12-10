from src.sendSongsVLC import sendSongsVLC
from src.searchSongs import searchSongs
from src.findXSPF import findXSPF
from src.randomizer import randomizer

print(sendSongsVLC(randomizer(searchSongs(findXSPF()))))