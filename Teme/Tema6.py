# Exercitii obligatorii

'''1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()'''

import math


class Cerc:
    import math

    raza = 0
    culoare = ''

    def __init__(self, r, c):
        self.raza = r
        self.culoare = c

    def descrie_cerc(self):
        print('Raza cercului este: ', self.raza)
        print('Culoarea cercului este: ', self.culoare)

    def aria(self):
        a = math.pi * (self.raza ** 2)
        print('Aria cercului este: ', a)

    def diametru(self):
        d = 2 * self.raza
        print('Diametrul cercului este: ', d)

    def circumferinta(self):
        c = 2 * math.pi * self.raza
        print('Circumferinta cercului este: ', c)


circle = Cerc(10, 'Verde')

circle.descrie_cerc()
circle.aria()
circle.diametru()
circle.circumferinta()

# --------------------------------------------------------------------------------------------------------------------

'''2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().'''


class Dreptunghi():
    lungime = 0
    latime = 0
    culoare = ''

    def __init__(self, L, l, c):
        self.lungime = L
        self.latime = l
        self.culoare = c

    def descrie(self):
        print('Lungimea cercului este: ', self.lungime)
        print('Latimea cercului este: ', self.latime)
        print('Culoarea cercului este: ', self.culoare)

    def aria(self):
        a = self.lungime * self.latime
        print('Aria cercului este: ', a)

    def perimetru(self):
        p = 2 * (self.lungime + self.latime)
        print('Perimetrul cercului este: ', p)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


dr = Dreptunghi(10, 5, 'Verde')

dr.descrie()
dr.aria()
dr.perimetru()
dr.schimba_culoarea('Albastru')
dr.descrie()

# --------------------------------------------------------------------------------------------------------------------

'''3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)'''


class Angajat():
    nume = ''
    prenume = ''
    salariu = 0

    def __init__(self, n, p, s):
        self.nume = n
        self.prenume = p
        self.salariu = s

    def descrie(self):
        print('Nume:', self.nume)
        print('Prenume:', self.prenume)
        print('Salariu:', self.salariu)

    def nume_complet(self):
        print('Numele complet este: ' + self.nume + ' ' + self.prenume)

    def salariu_lunar(self):
        print('Salariul lunar este:', self.salariu)

    def salariu_anual(self):
        print('Salariul anual este: ', self.salariu * 12)

    def marire_salariu(self, procent):
        marire = self.salariu * (procent / 100)
        noul_salariu = self.salariu + marire
        print(f'Noul salariu este {noul_salariu} lei, dupa marirea cu {marire} lei')


employer = Angajat('Popescu', 'Ion', 1000)

employer.descrie()
employer.nume_complet()
employer.salariu_lunar()
employer.salariu_anual()
employer.marire_salariu(25)

# --------------------------------------------------------------------------------------------------------------------

'''4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)'''


class Cont():
    iban = None
    titular_cont = ''
    sold = 0

    def __init__(self, i, t, s):
        self.iban = i
        self.titular_cont = t
        self.sold = s

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_sold(self, suma):
        self.sold = self.sold - suma
        print('Sold: ', self.sold)

    def creditare_sold(self, suma):
        self.sold = self.sold + suma
        print('Sold: ', self.sold)


account = Cont('ROOOBT456', 'Popescu Ion', 500)

account.afisare_sold()
account.debitare_sold(200)
account.creditare_sold(1500)
account.afisare_sold()

# --------------------------------------------------------------------------------------------------------------------

# Exercitii optionale

'''1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)

● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/'''


class Factura():
    seria = 'GAZ'
    numar = 0
    nume_produs = ''
    cantitate = 0
    pret_buc = 0

    def __init__(self, n, np, c, pb):
        self.numar = n
        self.nume_produs = np
        self.cantitate = c
        self.pret_buc = pb

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        return self.cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret
        return self.pret_buc

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        return self.nume_produs

    def tabel(self):
        from tabulate import tabulate
        from datetime import date
        table = [['Factura: Seria', self.seria, 'numar', self.numar], ['Data: ', date.today().strftime('%d/%m/%Y')],
                 ['Produs', '|', 'Cantitate', '|', 'Pret Bucata', '|', 'Total'],
                 [self.nume_produs, '|', self.cantitate, '|', self.pret_buc, '|', self.cantitate * self.pret_buc]]
        print(tabulate(table))


invoice = Factura(1234, 'Telefon', 7, 700)

invoice.tabel()
invoice.schimba_cantitatea(8)
invoice.schimba_nume_produs('Ceas')
invoice.schimba_pretul(200)
invoice.tabel()

# --------------------------------------------------------------------------------------------------------------------

'''2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0'''


class Masina():
    marca = 'Dacia'
    model = ''
    viteza_maxima = 0
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'alb', 'rosu', 'verde', 'albastru', 'galben'}
    inmatriculata = False

    def __init__(self, m, vm):
        self.model = m
        self.viteza_maxima = vm

    def descrie(self):
        print('Marca:', self.marca)
        print('Model:', self.model)
        print('Viteza maxima:', self.viteza_maxima)
        print('Viteza actuala:', self.viteza_actuala)
        print('Culoare:', self.culoare)
        print('Inmatriculata:', self.inmatriculata)

    def inmatriculare(self):
        if self.inmatriculata == False:
            self.inmatriculata = True
        return self.inmatriculata

    def vopseste(self, culoare):
        for i in self.culori_disponibile:
            if i == culoare:
                self.culoare = culoare
                break
            else:
                print('Culoarea nu este disponibila!!')
                break

    def accelereaza(self, viteza):
        if viteza < 0:
            print('EROARE!!!')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza
        return self.viteza_actuala

    def franeaza(self):
        self.viteza_actuala = 0
        return self.viteza_actuala


car = Masina('Sandero', 180)

car.descrie()
car.inmatriculare()
print('---------------')
car.vopseste('portocaliu')
car.accelereaza(200)
print('---------------')
car.descrie()

# --------------------------------------------------------------------------------------------------------------------

'''3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict'''


class TodoList():
    todo = {

    }

    def adauga_task(self, nume, descriere):
        self.todo.update({nume: descriere})

    def finalizeaza_task(self, nume):
        self.todo.pop(nume)

    def afiseaza_todo_list(self):
        for k in self.todo:
            print(k)

    def afiseaza_detalii_suplimentare(self, nume_task):
        answer = None
        if not nume_task in self.todo.keys():
            print('Task inexistent')
            answer = str(input(
                'Vreti sa adaugati task-ul? '))
            if answer.lower() == 'nu':
                print('La revedere')
            elif answer.lower() != 'nu':
                details = input('Care sunt detaliile task-ului? ')
                self.todo.update(({nume_task: details}))
            else:
                print('Task: ', nume_task, 'Detalii: ', self.todo[nume_task])


x = TodoList()

x.adauga_task('spalat', 'haine in masina de spalat')
x.adauga_task('aspirat', 'aspira in living')
x.afiseaza_todo_list()
x.afiseaza_detalii_suplimentare('uscat')
