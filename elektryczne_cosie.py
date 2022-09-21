import os, sys, subprocess

print("Definicja oporu elektrycznego przewodnika - wpisz (1) ")
print("Natezenie pradu elektrycznego - wpisz (2) ")
print("Pojemnosc kondensatora - wpisz (3)")
print("pojemnosc przewodnika - wpisz (4)")
print("praca pradu elektrycznego - wpisz (5)")
print("energia pola elektrostatycznego - wpisz (6)\n")
obl = input("co chcesz obliczyć? ")
if obl == "1":
    U = input("wpisz wartosc napiecia na koncach przewodnika (w voltach). ")
    I = input("wpisz wartosc natezenia pradu plynacego przez przewodnik (w amperach). ")
    U = float(U)
    I = float(I)
    R = U / I
    R = str(R)
    print("opor przewodnika wynosi: " + R + "\u03A9")
    print(" ")
    rep = input("cos jeszcze do obliczania? (tak/nie) ")
    if rep == "tak":
        print("\n")
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
                        sys.argv[1:])
    else:
        quit()
else:
    if obl == "2":
        QN = input("wpisz wartosc ladunku przeplywajacego przez przewodnik (w coulombach). ")
        TN = input("wpisz czas przeplywu pradu (w sekundach). ")
        QN = float(QN)
        TN = float(TN)
        IN = QN / TN
        IN = str(IN)
        print("natezenie pradu elektrycznego wynosi: " + IN + "A")
        print(" ")
        rep = input("cos jeszcze do obliczania? (tak/nie) ")
        if rep == "tak":
            print("\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
                            sys.argv[1:])
        else:
            quit()
    else:
        if obl == "3":
            QPK = input("wpisz wartosc ladunku zgromadzonego na przewodniku (w faradach). ")
            UPK = input("wpisz wartosc napiecia miedzy okladkami kondensatora (w voltach). ")
            QPK = float(QPK)
            UPK = float(UPK)
            CPK = QPK / UPK
            CPK = str(CPK)
            print("pojemnosc kondensatora wynosi: " + CPK + "F")
            print(" ")
            rep = input("cos jeszcze do obliczania? (tak/nie) ")
            if rep == "tak":
                print("\n")
                subprocess.call([sys.executable, os.path.realpath(__file__)] +
                                sys.argv[1:])
            else:
                quit()
        else:
            if obl == "4":
                QPP = input("wpisz wartosc ladunku zgromadzonego na przewodniku (w faradach). ")
                VPP = input("wpisz wartosc potencjalu przewodnika po wprowadzeniu na niego powyzszego ladunku (w voltach) ")
                QPP = float(QPP)
                VPP = float(VPP)
                CPP = QPP / VPP
                CPP = str(CPP)
                print("pojemnosc przewodnika wynosi " + CPP + "F")
                print(" ")
                rep = input("cos jeszcze do obliczania? (tak/nie) ")
                if rep == "tak":
                    print("\n")
                    subprocess.call([sys.executable, os.path.realpath(__file__)] +
                                    sys.argv[1:])
                else:
                    quit()
            else:
                if obl == "5":
                    U5 = input("wpisz wartosc napiecia na koncach przewodnika (w voltach). ")
                    I5 = input("wpisz wartosc natezenia pradu plynacego przez przewodnik (w amperach). ")
                    T5 = input("wpisz czas przeplywu pradu (w sekundach). ")
                    U5 = float(U5)
                    I5 = float(I5)
                    T5 = float(T5)
                    W5 = U5 * I5 * T5
                    W5 = str(W5)
                    print("praca pradu elektrostatycznego wynosi: " + W5 + "W")
                    print(" ")
                    rep = input("cos jeszcze do obliczania? (tak/nie) ")
                    if rep == "tak":
                        print("\n")
                        subprocess.call([sys.executable, os.path.realpath(__file__)] +
                                        sys.argv[1:])
                    else:
                        quit()
                else:
                    if obl == "6":
                        Q6 = input("wpisz wartosc ladunku (w coulombach). ")
                        C6 = input("wpisz wartosc pojemnosci (w faradach). ")
                        Q6 = float(Q6)
                        C6 = float(C6)
                        E6I = Q6 ** 2 / C6
                        E6 = E6I / 2
                        E6 = str(E6)
                        print("energia pola elektrostatycznego wynosi: " + E6 + "W")
                        print(" ")
                        rep = input("cos jeszcze do obliczania? (tak/nie) ")
                        if rep == "tak":
                            print("\n")
                            subprocess.call([sys.executable, os.path.realpath(__file__)] +
                                            sys.argv[1:])
                        else:
                            quit()
                    else:
                        repdef = input("bledna wartosc, aby powtorzyc proces wpisz (r). ")
                        if repdef == "r":
                            print(" \n")
                            subprocess.call([sys.executable, os.path.realpath(__file__)] +
                                        sys.argv[1:])
                        else:
                            quit()
