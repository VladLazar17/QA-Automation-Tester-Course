# for i in range(999):
#     if i == 4:
#         break
#     print(i)

# for i in range (15):
#     if i == 5 or i == 13:
#         continue
#     print(i)

# index = 3
#
# while index <= 10:
#     index += 1
#     print(index)

lista = ['Andrei', 'Vlad', 'Alex', 'Vlad', 'Mihai', 'Maria', 'Ionela']

# for nume in lista:
#     if nume == 'Mihai':
#         for litera in nume:
#             print(litera)
# y = 1
# x = 20
#
# while x <= 30:
#     y += 1
#     if y == 5:
#         break
#     print('Am ajuns aici')
#
# x = 20
#
# while x <= 30:
#     x += 1
#     print('Am ajuns aici')
#
# while x <= 30:
#     x += 1
#     print('Am ajuns aici')

car = {"Make": "Honda",
       "Model": "Civic",
       "Color": "Black",
       "Year": 2019
       }

# for index in car:
#     print(car[index])

# for masina in car.values():
#     print(masina)
# print(type(car.values()))
'''
string = 'abcdefghiklmnopqrstz'
lista = [i for i in string]
# print(len(lista))
EchipaA = []
EchipaB = []
# print(lista)

for i in range(len(string)):
    if i % 2 == 0:
        EchipaA.append(lista[i])
    elif i % 2 != 0:
        EchipaB.append(lista[i])
print(EchipaA)
print(EchipaB)
'''

string = 'abcdefghiklmnopqrstz'
lista = [i for i in string]
# print(len(lista))
EchipaA = []
EchipaB = []
# print(lista)

# for i in range(len(string)) :
# print(len(string))
# print(i)
for i in range(0, 20, 2):
    EchipaA.insert(i,lista[i])
    lista.remove(i)
EchipaB = lista

print(EchipaA)
print(EchipaB)
