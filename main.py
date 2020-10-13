import powitanie_zasady as wstep
from random import randint

moj_znak = " "
enemy_znak = " "

# punkty
ja = 0
enemy = 0

# baza znakow
kamien = ["kamien", "KAMIEN", "Kamien", "k", "K", "kamień", "KAMIEŃ"]
papier = ["papier", "PAPIER", "Papier", "p", "P"]
nozyce = ["nozyce", "NOZYCE", "Nozyce", "n", "N", "nożyce", "NOŻYCE"]


# sprawdzanie czy podany znak jest w bazie znakow
def znak_kam_pap_noz(znak_uzytk):
    for znak in kamien:
        if znak_uzytk == znak:
            return "kamien"
    for znak in papier:
        if znak_uzytk == znak:
            return "papier"
    for znak in nozyce:
        if znak_uzytk == znak:
            return "nozyce"


# losowanie ruchu wroga
def ruch_wroga():
    global enemy_znak
    numer = randint(1, 3)
    if numer == 1:
        enemy_znak = "kamien"
    elif numer == 2:
        enemy_znak = "papier"
    elif numer == 3:
        enemy_znak = "nozyce"
    else:
        print("Przeciwnik ma problem z swoim ruchem")


# zliczanie punktow
def wygrana():
    global ja
    print("Wygrana!")
    ja += 1


def przegrana():
    global enemy
    print("Przegrana...")
    enemy += 1


def remis():
    global ja
    global enemy
    print("REMIS!")
    ja += 1
    enemy += 1


ilosc_prob = int(wstep.powitanie_zasady())
while ilosc_prob >= 1:
    ilosc_prob -= 1

    # losowanie znaku przeciwnika
    ruch_wroga()

    # zczytanie znaku i określenie go
    moj_znak = input("Dej znak: ")
    moj_znak = znak_kam_pap_noz(moj_znak)

    if enemy_znak == moj_znak:
        remis()
    elif enemy_znak == "kamien" and moj_znak == "papier":
        wygrana()
    elif enemy_znak == "kamien" and moj_znak == "nozyce":
        przegrana()
    elif enemy_znak == "papier" and moj_znak == "nozyce":
        wygrana()
    elif enemy_znak == "papier" and moj_znak == "kamien":
        przegrana()
    elif enemy_znak == "nozyce" and moj_znak == "kamien":
        wygrana()
    elif enemy_znak == "nozyce" and moj_znak == "papier":
        przegrana()
    else:
        print("Coś, coś poszło nie tak...")
        ilosc_prob += 1
print("Wynik: {} : {}".format(ja, enemy))

# TODO 1: # done # losowanie ruchu przeciwnika
# TODO 2: # done # system swojego wyboru
# TODO 3: # done # naprawic zliczanie punktow
# TODO 4: # done # zrobic for ktory sprawdza czy podany znak jest w bazie znakow
# TODO 5: # done # naprawić TODO 4
# TODO 7: # done # zabezpieczyć kod przed wprowadzeniem znaku nieznajdującego się w żadnej bazie
# TODO 6: #      #
