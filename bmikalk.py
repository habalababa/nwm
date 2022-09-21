print("witamy w najnowoczesniejszym kalkulatorze bmi ze swietnym, oldschoolowym interfacem")
wzrost = input("1. wpisz swoj wzrost w cm ")
waga = input("2. wpisz swoja wage w kg ")
wzrost = float(wzrost)
waga = float(waga)
bmi = waga / wzrost ** 2 * 10000
bmi = int(bmi)
if bmi < 16:
    bmi = str(bmi)
    print("twoje bmi wynosi " + bmi + ".\noznacza to wyglodzenie.")
    bmi = int(bmi)
else:
    if bmi >= 16 and bmi < 17:
        bmi = str(bmi)
        print("twoje bmi wynosi " + bmi + ".\noznacza to wychudzenie.")
        bmi = int(bmi)
    else:
        if bmi >= 17 and bmi < 18.5:
            bmi = str(bmi)
            print("twoje bmi wynosi " + bmi + ".\noznacza to niedowage.")
            bmi = int(bmi)
        else:
            if bmi >= 18.5 and bmi < 25:
                bmi = str(bmi)
                print("twoje bmi wynosi " + bmi + ".\noznacza to wage prawidlowa.")
                bmi = int(bmi)
            else:
                if bmi >= 25 and bmi < 30:
                    bmi = str(bmi)
                    print("twoje bmi wynosi " + bmi + ".\noznacza to nadwage.")
                    bmi = int(bmi)
                else:
                    if bmi >= 30 and bmi < 35:
                        bmi = str(bmi)
                        print("twoje bmi wynosi " + bmi + ".\noznacza to 1 stopien otylosci.")
                        bmi = int(bmi)
                    else:
                        if bmi >= 35 and bmi < 40:
                            bmi = str(bmi)
                            print("twoje bmi wynosi " + bmi + ".\noznacza to 2 stopien otylosci.")
                            bmi = int(bmi)
                        else:
                            if bmi >= 40:
                                bmi = str(bmi)
                                print("twoje bmi wynosi " + bmi + ".\noznacza to skrajna otylosc.")
                            else:
                                print("blad")
                                input()
input()