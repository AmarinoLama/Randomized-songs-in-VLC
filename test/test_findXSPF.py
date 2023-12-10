from src.findXSPF import findXSPF

import os

userName = os.getenv('USERNAME')

def test_xspfExist():
    assert findXSPF() is not None

def test_correctFormat():
    assert findXSPF().startswith(r"C:\\")
    assert findXSPF().endswith(".xspf")
    assert isinstance(findXSPF(), str)

# caso test para cuando el xspf está dentro del proyecto (caso particular, si se hace este otros fallarán)

def test_xspfInProyect():
    assert findXSPF().startswith(r"C:\\Users\\"+ userName + r"\\Desktop\\proyectoVLC\\Randomized-songs-in-VLC\\")

# caso test para cuando el xspf está en la carpeta de música (caso particular, si se hace este otros fallarán)

def test_outProyet():
    assert findXSPF().startswith(r'C:\\Users\\' + userName + r'\\Music')

# caso test para cuando no encuentra el xspf (caso particular, si se hace este otros fallarán)

def test_xspfNotFound():
    assert findXSPF() == None