def citireLista():
    """
    primeste un nr n
    primeste n nr
    :return: returneaza o lista de n nr
    """
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l

def nrPozitie(l,x,n):
    """
    reutrneaza daca un nr x se gaseste in lista l dupa pozitia n
    param l : lista
    :param x: nr pe care il cautam dupa o anumita pozitie
    :param n: pozitia dupa care cautam numarul
    :return: True or False daca se gaseste nr x dupa pozitia n
    """

    for i in range (n,len(l)):
        if l[i] == x:
            return True
    return False
def testNrPozitie():
    assert nrPozitie([12,13,14],13,1) is True
    assert nrPozitie([12, 13, 14], 12, 1) is False
testNrPozitie()

def sumaNrPare(l):
    """
    calculeaza suma numerelor are din lsita
    :param l: lista
    :return: suma numerelor are din lsita
    """
    s=0
    for x in l:
        if x%2==0:
            s=s+x
    return s
def testSumaNrPare():
    assert sumaNrPare([12,13,14,2])==28
    assert sumaNrPare([11, 13, 14, 2]) == 16
testSumaNrPare()

def afisareNrPare(l):
    """
    afiseaza toate numerele pare din lista
    :param l: lista
    :return: lista cu nrpare din lista
    """
    rezulta=[]
    for z in l:
        if z%2==0:
            rezulta.append(z)
    return rezulta
def testAfisareNrPare():
    assert afisareNrPare([12,13,14,15,16]) == [12,14,16]
    assert afisareNrPare([23, 12, 3, 52, 12]) == [12,52,12]
testAfisareNrPare()

def main():
    while True:
        print("1. Citire lista")
        print("a. afisare lista")
        print("2. gasire element x dupa pozitia n")
        print("3. suma nr pare din lista")
        print("4. afisare nr pare din lista")
        print("x. iesire meniu")

        optiune = input("Dati optiunea: ")
        if optiune == "1":
            li =citireLista()
        elif optiune == "2":
            y = int(input("dati nr pe care doriti sa il cautati in lista:"))
            m = int(input("dati nr pozitie dupa care il cautati pe y:"))
            if nrPozitie(li,y,m) is True:
                print("DA")
            else:
                print("NU")
        elif optiune == "3":
            print(sumaNrPare(li))
        elif optiune == "4":
            print(afisareNrPare(li))
        elif optiune =="a":
            print(li)
        elif optiune == "x":
            break
        else:
            print("optiune gresita incercati din nou")
main()
