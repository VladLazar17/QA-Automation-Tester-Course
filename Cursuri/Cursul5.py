# def hi():
#     print('Hi!')
#
# hi()
# hi('Test')
#-----------------------------------------------------------------

# def hi(user):
#     print('Hi!')
#
# # hi()
# hi('Test')
#------------------------------------------------------------------

#Verifica ca variabila este string

# x = int(input('Introduceti o variabila: '))
#
# def verificare_numar(user):
#
#
# def verifica_variabila(user):
#     print(type(user))
#     if type(user) == str:
#         print(f'Variabila {user} este un {type(user)}')
#     elif type(user) != str:
#         user2 = user
#         user = str(user)
#         print(f'Variabila {user} a fost convertita din {type(user2)} in {type(user)}')
#         return user
#     else:
#         print(f'Variabila este goala')
#
# verifica_variabila(x)
#------------------------------------------------------------------

# x = int(input('x = '))
# y = int(input('y = '))
#
# def suma(a,b):
#     z = a + b
#     return z
#
# def suma2(h):
#     d = h + suma(5, 6)
#     return d
#
# print(suma2(suma(x,y)))

#------------------------------------------------------------------
'''16. Functie care primesete 2 liste de numere (numerele pot fi dublate)
Returnati numerele comune 

Ex:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}'''

# raspuns = []
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
#
# def functie(l1,l2):
#     for i in range(len(l1)):
#         for j in range(len(l2)):
#             if l1[i] == l2[j]:
#                 raspuns.append(l1[i])
#     return raspuns
#
# print(set(functie(list1,list2)))

#------------------------------------------------------------------

# def create_a_list(list):
#     list2 = str(list)
#     list2 = list2.split(',')
#     return list2
# x = create_a_list('5,4,3,2')
#
# print(x)
# print(type(x))

#------------------------------------------------------------------


# l = int(input('Lungimea listei este: '))
# list = []
#
# for i in range(l):
#     x = input('Introdu` un element in lista: ')
#     list.append(x)
# print(list)

#------------------------------------------------------------------

list = []
def creare_list(l):
    while 1 != 0:
        x = input('Introdu` un element in lista: ')
        if x == '':
            break
        l.append(int(x))
    return l

print(creare_list(list))

#------------------------------------------------------------------