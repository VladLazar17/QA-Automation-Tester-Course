# Exercitii obligatorii

'''1.Funcție care să calculeze și să returneze suma a două numere'''

def suma(x,y):
    z = x + y
    return z
print(suma(11,13))

'''2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar'''

x = int(input('Introduceti un numar: '))

def par_impar(numar):
    if numar % 2 == 0:
        print('TRUE')
    else:
        print('FALSE')

par_impar(x)

'''3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)'''

x = input('Introduceti numele dvs compelet: ')


def nr_caractere(nume):
    y = 0
    for i in nume:
        if i != ' ':
            y += 1
    return y


print(f'Numele tau are {nr_caractere(x)} caractere')

'''4. Funcție care returnează aria dreptunghiului'''

L = int(input('Introduceti lungimea dreptunghiului: '))
l = int(input('Introduceti latimea dreptunghiului: '))


def aria_dreptunghi(a, b):
    c = a * b
    return c


print(f'Aria dreptunghiului este {aria_dreptunghi(L, l)} ')

'''5. Funcție care returnează aria cercului'''

r = int(input('Introduceti raza cercului: '))


def aria_cerc(raza):
    a = 3.1415 * (raza ** 2)
    return a


print(f'Aria cercului este {aria_cerc(r)} ')

'''6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.'''

string = input('Introduceti un string: ')
caracter = input('Introduceti un caracter: ')


def gasire_caracter(a, b):
    if b in a:
        print('True')
    else:
        print('False')


gasire_caracter(string, caracter)

'''7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y'''

x = input('Introduceti un string: ')


def caractere(a):
    y = 0
    z = 0
    for i in a:
        if i != ' ' and str(i).isupper():
            y += 1
        elif i != ' ' and str(i).islower():
            z += 1

    print(f'Numarul de caractere lower case este {z}')
    print(f'Numarul de caractere upper case este {y}')


caractere(x)

'''8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive'''

def lista_pozitive(l):
    pozitive = []
    for i in l:
        if i > 0:
            pozitive.append(i)
    return pozitive


list = [1, 2, 3, -6, -9, 5, -5]

print(lista_pozitive(list))


'''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.'''

a = input('Introduceti un numar: ')
b = input('Introduceti un numar: ')

def comparare_numere(x, y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    elif x < y:
        print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
    else:
        print('Numerele sunt egale')

comparare_numere(a, b)

'''10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False'''

numere = {1, 2, 3, 4, 5}
x = int(input('Introduceti un numar: '))


def adaugare_numar(s, n):
    if n in s:
        print('Nu am adaugat numarul nou in set. Acesta exista deja')
        return False
    else:
        s.add(n)
        print(f'Am adaugat numarul nou {n} in set')
        return True


print(adaugare_numar(numere, x))


# Exercitii optionale

'''1. Funcție care primește o lună din an și returnează câte zile are acea luna'''

x = input('Introduceti luna: ')

def zile_luna(luna):
    luni ={
        'Ianuarie' : 31,
        'Februarie' : 28,
        'Martie' : 31,
        'Aprilie' : 30,
        'Mai' : 31,
        'Iunie' : 30,
        'Iulie' : 31,
        'August' : 31,
        'Septembrie' : 30,
        'Octombrie' : 31,
        'Noiembrie' : 30,
        'Decembrie' : 31
    }
    if luna in luni:
        l = luni.get(luna)
    return l

print(f'Luna {x} are {zile_luna(x)} zile')


'''2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
● print("Suma: ", a)

● print("Diferenta: ", b)
● print("Inmultirea: ", c)
● print("Impartirea: ", d)'''

def calculator(x,y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

a, b, c, d = calculator(10, 2)

print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


'''3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}'''

def numarare_cifre(lista_numere):
    dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }
    for i in dict.keys():
        for j in lista_numere:
            if i == j:
                dict[i] = dict[i] + 1
    return dict


print(numarare_cifre([1, 2, 3, 3, 5, 1, 1, 5, 6, 7, 8, 9, 9, 0, 0]))


'''4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele'''

a = input('Introduceti un numar: ')
b = input('Introduceti un numar: ')
c = input('Introduceti un numar: ')

def maxim(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    else:
        print(z)

maxim(a, b, c)

'''5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)'''

a = int(input('Introduceti un numar: '))


def suma_Gauss(x):
    sum = 0
    for i in range(0, x + 1):
        sum = sum + i
    return sum


print(suma_Gauss(a))


# Exercitii bonus

'''1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune

Exemplu:
list1 = [1, 1, 2, 3]

list2 = [2, 2, 3, 4]
Răspuns: {2, 3}'''

list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]

def intersec(l1,l2):
    k = []
    for i in l1:
        for j in l2:
            if i == j:
                k.append(i)
    print(set(k))

intersec(list1,list2)

'''2.. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.'''

x = int(input('Introduceti un pret: '))
y = int(input('Introduceti reducerea: '))


def reducere(pret, reducere):
    if reducere > 100 or reducere < 0:
        print('Reducerea este invalida!!!')
    else:
        pret = pret - (reducere / 100 * pret )
        print(pret)

reducere(x,y)


'''3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)'''

from datetime import datetime
import pytz

def current_date():
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print('Data si ora:', dt)
    dt_china = pytz.timezone('Asia/Hong_Kong')
    china = datetime.now(dt_china).strftime("%d/%m/%Y %H:%M:%S")
    print('Data si ora in China: ', china)


current_date()


'''4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)'''

from datetime import date

def zile_craciun(an):
    craciun = date(year = an, month = 12, day = 25)
    azi = date.today()
    zile = (craciun - azi).days
    print(f'Mai sunt {zile} zile pana la Craciun')

zile_craciun(2030)