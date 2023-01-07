# a = 5
# b = 3
# a+=a*(b+2)
# # a = a + [a*(b+2)]
# print(a)

# propozitie = 'Ana are mere.'
# fructe = 'mere '
# nume = 'Ana'
# # print(propozitie[len(propozitie)-2:7:-1])
# if fructe == 'mere' and nume == 'Ana':
#     print('Ana are 5 mere.')
# elif fructe == 'mere' or nume == 'Ana':
#         if fructe == 'mere':
#             print('Fructele sunt mere.')
#         if nume == 'Ana':
#             print('Numele este Ana')
# else:
#     print('Ana nu are mere.')

'''
propozitie = 'Ana are mere.'

# print(propozitie[5:len(propozitie)])
# print(propozitie[5::-1])
numar_spatii = propozitie.count(' ')
# print(propozitie.split(' '))
for index in propozitie.split(' '):
    if index == 'mere.':
        print(index[:len(index)-1])
    elif index != 'mere.':
        print(index)
'''

# import pyautogui as py
# import time
#
# message = "Stefan a zis: MIMI VREAU SA FACI DE MANCAREE!"
# count = 1
#
# time.sleep(2)
#
# for i in range(len(message)):
#     py.typewrite(message)
#     py.press('Enter')
#     # time.sleep(2)
# # py.typewrite("Ce zici?")
# # py.press('Enter')

echipa = ['Alex', 'Vlad', 'Daniel', 'Tudor', 'Lucian']
schimbari_efectuate = 0
schimbari_max = 3
print(f'Echipa din teren este: {echipa} ')
jucator_teren = input('Introduceti numele jucatorului pe care vreti sa il inlocuiti: ')

if jucator_teren in echipa and schimbari_efectuate <= schimbari_max:
    jucator_schimbare = input('Introduceti numele jucatorului pe care vreti sa il introduceti: ')
    echipa.remove(jucator_teren)
    echipa.append(jucator_schimbare)
    schimbari_efectuate = schimbari_efectuate + 1
    print('A intrat ' + str(jucator_schimbare) + ' a ieșit ' + str(jucator_teren) + ' mai ai ' + str(3-schimbari_efectuate) + ' schimbări')
else:
    print('Nu se poate efectua schimbarea deoarece jucătorul x nu e în teren')