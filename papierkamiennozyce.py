import random
def tablica():
    print("twoje punkty:", tywin)
    print("punkty komputera:", pcwin)
    print("remisy:", remis)
    print("komputer wybral:", pcwybor)
    print(" ")
tywin = 0
pcwin = 0
remis = 0
opcje = ["papier", "kamien", "nozyce"]
print("gra papier kamien nozyce\n")
while True:
    wybor = input("wpisz papier/kamien/nozyce, lub q aby wyjsc ")
    if wybor == "q":
        break
    if wybor not in opcje:
        print("wpisz opcje poprawnie")
        continue
    lospc = random.randint(0, 2)
    pcwybor = opcje[lospc]
    if wybor == "papier" and pcwybor == "kamien":
        tywin += 1
        print("wygrales")
        tablica()
        continue
    elif wybor == "nozyce" and pcwybor == "papier":
        tywin += 1
        print("wygrales")
        tablica()
        continue
    elif wybor == "kamien" and pcwybor == "nozyce":
        tywin += 1
        print("wygrales")
        tablica()
        continue
    elif wybor == pcwybor:
        remis += 1
        print("remis")
        tablica()
        continue
    else:
        pcwin += 1
        print("przegrales")
        tablica()
        continue