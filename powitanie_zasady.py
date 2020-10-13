from time import sleep

def powitanie_zasady():
    print("Witaj w \"Kamień, Papier, Nożyce\"!")
    print("Wybierasz swój ruch wpisując \"kamień\", \"papier\" lub \"nożyce\".")
    print("... albo po prostu wpisując pierwsze litery.")
    wybrana_ilosc_prob = input("Ile rund chcesz grać? Podaj: ")
    print("Awięc grasz do {} prób, tyle ile wybrałeś.".format(wybrana_ilosc_prob))
    print("Powodzenia!")
    sleep(1)
    return wybrana_ilosc_prob
