# EXERCITII OBLIGATORII

x = int(input('Introduceti un numar: '))
y = int(input('Introduceti un numar: '))
z = int(input('Introduceti un numar: '))

'''1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.'''

# IF ELSE - Daca se indeplineste conditia se executa codul 1, daca nu se executa codul 2.

'''2. Verifică și afișează dacă x este număr natural sau nu.'''

if x >= 0:
    print(f'{x} este numar natural.')
else:
    print(f'{x} nu este numar natural.')

'''3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.'''

if x > 0:
    print(f'{x} este numar pozitiv.')
elif x < 0:
    print(f'{x} este numar negativ.')
else:
    print(f'{x} este numar neutru.')

'''4. Verifică și afișează dacă x este între -2 și 13.'''

if x >= -2 and x <= 13:
    print(f'{x} este intre -2 si 13')
else:
    print(f'{x} nu este intre -2 si 13')

'''5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.'''

if x-y < 5:
    print(f'Diferenta dintre {x} si {y} este mai mica decat 5.')
else:
    print(f'Diferenta dintre {x} si {y} nu este mai mica decat 5.')

'''6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.'''

if not(x >= 5 and x <= 27):
    print(f'{x} nu este intre 5 si 27')
else:
    print(f'{x} este intre 5 si 27')

'''7. x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.'''

if x == y:
    print(f'{x} este egal cu {y}')
elif x > y:
    print(f'{x} este mai mare decat {y}')
else:
    print(f'{x} este mai mic decat {y}')

'''8. X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.'''

if x == y and y == z:
    print('Triunghi echilateral')
elif x != y and y!= z and x != z:
    print("Triunghi oarecare")
else:
    print("Triunghi isoscel")

'''9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu'''

a = str(input('Introduceti o litera: '))
if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print(a + ' este o vocala.')
else:
    print(a + ' este o consoana.')

'''10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F'''

nota = int(input('Introduceti nota: '))
if nota <= 10 and nota >= 9:
    print('Ai luat nota A.')
elif nota < 9 and nota >= 8:
    print('Ai luat nota B.')
elif nota < 8 and nota >= 7:
    print('Ai luat nota C.')
elif nota < 7 and nota >= 6:
    print('Ai luat nota D.')
elif nota < 6 and nota >= 4:
    print('Ai luat nota E.')
elif nota < 4 and nota >= 0:
    print('Ai luat nota F.')
else:
    print('Nota nu este valida!!!')


# EXERCITII OPTIONALE

'''1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)'''

x = int(input('Introduceti un nr: '))
if len(str(x)) >= 4:
    print(f'{x} are 4 cifre.')
else:
    print(f'{x} nu are minim 4 cifre.')

'''2.Verifică dacă x are exact 6 cifre.'''

x = int(input('Introduceti un nr: '))
if len(str(x)) == 6:
    print(f'{x} are exact 6 cifre.')
else:
    print(f'{x} nu are exact 6 cifre.')

'''3.Verifică dacă x este număr par sau impar (x e int).'''

x = int(input('Introduceti un nr: '))
if x % 2 == 0:
    print(f'{x} este numar par.')
else:
    print(f'{x} este numar impar.')

'''4. x, y, z (int)
Afișează care este cel mai mare dintre ele?'''

x = int(input('Introduceti un numar: '))
y = int(input('Introduceti un numar: '))
z = int(input('Introduceti un numar: '))

if x > y and x > z:
    print(f'{x} este cel mai mare numar dintre {x}, {y}, {z}.')
elif y > z and y > x:
    print(f'{y} este cel mai mare numar dintre {x}, {y}, {z}.')
elif z > x and z > y:
    print(f'{z} este cel mai mare numar dintre {x}, {y}, {z}.')
else:
    print('Cel putin 2 numere sunt egale')

'''5. X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.'''

x = int(input('Introduceti un numar: '))
y = int(input('Introduceti un numar: '))
z = int(input('Introduceti un numar: '))

if x < 180 and x > 0 and x + y + z == 180:
    print('Triunghiul este valid.')
elif y < 180 and y > 0 and x + y + z == 180 :
    print('Triunghiul este valid.')
elif z < 180 and z > 0 and x + y + z == 180 :
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid')

'''6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte' '''

propozitie = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introduceti un numar: '))
print(propozitie[0:len(propozitie)-x])

'''7.Același string. Declară un string nou care să fie format din primele 5 caractere
+ ultimele 5'''

substring = propozitie[0:5] + propozitie[len(propozitie)-5:]
print(substring)

'''8. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest ' '''

word = 'rock'
index = propozitie.find(word)
print(propozitie[0:index])

'''9. Citește de la tastatura un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat'''

string = input('Introduceti un cuvant: ')
assert string[0].lower() == string[len(string)-1].lower() , print('Fals - prima si ultima litera NU sunt la fel')
print('Adevarat - prima si ultima litera sunt la fel')



'''10. Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)'''

numere = '0123456789'
print('Numerele pare sunt: ' + numere[0:len(numere):2])
print('Numerele impare sunt: ' + numere[1:len(numere):2])


# Exerciții Bonus (may need google) .

'''11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y'''

import random

pc_dice_roll = random.randint(1,6)
dice_roll = int(input('Introduceti un numar de la 1 la 6: '))

if pc_dice_roll > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {dice_roll} dar a fost {pc_dice_roll}')
elif pc_dice_roll < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {dice_roll} dar a fost {pc_dice_roll}')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {dice_roll} si zarul a fost {pc_dice_roll}')

