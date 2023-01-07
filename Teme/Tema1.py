#Exercitii obligatorii

'''1. In cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# O variabila este o locatie din memorie in care putem atribui valori'''

'''2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :

- string
- int
- float
- bool

Observație: Valorile vor fi alese de tine după preferințe.'''

nume_elev = 'Vlad'
numar_prezente = 15
nota = 9.55
prezent = True

'''3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.'''

print(type(nume_elev))
print(type(numar_prezente))
print(type(nota))
print(type(prezent))

'''4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.'''

nota = round(nota)
print(nota)
print(type(nota))

'''5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.'''

print(f'Elevul {nume_elev} are {numar_prezente} prezente si a primit nota {nota} . Este prezent? {prezent}')

'''6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.'''


numele = input('Numele: ')
prenumele = input('Preumele: ')

x = (len(numele)+len(prenumele))
print(f'Numele complet are {x} caractere.')

'''7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.'''

lungimea = input('Lungimea dreptunghiului este: ')
latimea = input('Lungimea dreptunghiului este: ')

aria = int(lungimea)*int(latimea)
print('Aria dreptunghiului este ', aria)

'''8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';'''

fraza = 'Coral is either the stupidest animal or the smartest rock'
print(fraza.count(" the "))

'''9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.'''

z = fraza.count(" the ")
print(f'Cuvantul `the` apare de {z} ori')

'''10. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.'''

assert type(fraza) == int


#Exercitii optionale

'''1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.'''

cuvant = input('String impar: ')
mij = round(len(cuvant) / 2)
print(cuvant[mij])

'''2. Folosind assert, verifică dacă un string este palindrom.'''

cuv = input('Introduceti un cuvant: ')
assert (cuv==cuv[::-1])
print('Este palindrom')

'''3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.'''

a, b = input('Introduceti 2 cuvinte: ').split()
print('a = '+a+' b = '+b)

'''
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''

word = input('Introduceti un string: ')
x = word[0]
y = word[1:(len(word)-1)]
print(x + y.replace(x, x.upper())+word[(len(word)-1)])

'''5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****'''

user = input('Introduceti userul: ')
password = input('Introduceti o parola: ')
print('Parola pt userul '+user+' este '+str(password.replace(password, '*') * len(password))+' si are '+str(len(password))+' caractere.')