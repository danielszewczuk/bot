import random
from ping3 import ping as ping3_ping

def losuj(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        linie = plik.readlines()
        wylosowana_linia = random.choice(linie)
        return wylosowana_linia.strip()

def isItUp(adres):
    response = ping3_ping(adres)   
    if response is not None and response is not False:
        response = response * 1000
        response = round(response, 2)
        return True
    else:
        return False