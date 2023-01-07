# Exercitii obligatorii

'''1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
    print('Masina mea preferata este', masini[i])

for masina in masini:
    print('Masina mea preferata este', masina)

i = 0
while i < len(masini):
    print('Masina mea preferata este', masini[i])
    i += 1

'''2. Aceeași listă:
Folosește un for else
În for

- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.'''

for i in range(len(masini)):
    if i == 0 or i == len(masini) - 1:
        masini[i] = masini[i]
    else:
        masini[i] = masini[i].upper()
else:
    print(masini)

'''3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘'''

for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina dorita de dvs.')
        break
    else:
        print('Am gasit masina', masina, '. Mai cautam.')

'''4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.'''

for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lastun':
        continue
    print('S-ar putea sa va placa masina', masini[i])

'''5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.'''

x = 'Tesla'
masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'Lastun' or masini[i] == 'Trabant':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'

print('Modele vechi:', masini_vechi)
print('Modele noi:', masini)

'''6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.'''

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000,
}

for key, value in pret_masini.items():
    if value <= 15000:
        print('Pentru un buget de sub 15000 euro puteti alege masina', key)

'''7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

count = 0

for i in numere:
    if i == 3:
        count += 1;
print('Numarul 3 apare de', count, 'ori')

'''8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).'''

suma = 0
for numar in numere:
    suma += numar
print('Suma numerelor este', suma)

'''9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).'''

max = 0
for i in range(len(numere)):
    if numere[i] > max:
        max = numere[i]
print('Cel mai mare numar este:', max)

'''10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.'''

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = numere[i] * (-1)
print(numere)

# Exercitii Optionale

'''1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
    if i > 0:
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)
print('Numere pare sunt:', numere_pare)
print('Numere impare sunt:', numere_impare)
print('Numere pozitive sunt:', numere_pozitive)
print('Numere negative sunt:', numere_negative)

'''2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.'''

numere_crescator = 0

for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            numere_crescator = alte_numere[i]
            alte_numere[i] = alte_numere[j]
            alte_numere[j] = numere_crescator
print(alte_numere)

'''3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!'''

import random

numar_secret = random.randint(1, 30)
numar_ghicit = None

while numar_secret != numar_ghicit:
    numar_ghicit = int(input('Introduceti un numar: '))
    if numar_ghicit < numar_secret:
        print('Nr secret e mai mare')
    elif numar_ghicit > numar_secret:
        print('Nr secret e mai mic')
    else:
        print('Felicitari! Ai ghicit numarul!')
        break

'''4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333'''

numar = int(input('Alegeti un numar: '))

for i in range(1, numar + 1):
    print(str(i) * i)

'''5.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)'''

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print('Cifra curenta este: ', tastatura_telefon[i][j])
