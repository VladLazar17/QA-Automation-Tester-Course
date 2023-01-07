#List

# variabila = (1, 4)
# list = (1 , 7)
# print(variabila)

# variabila.append('vara')
#
# print(variabila)
#
# print(type(variabila))

# print(variabila + list)
# variabila2 = variabila.count()
# print(variabila2)


# masina = {'culoare', 'roti', 'lungime', 'latime', 'culoare'}
# print(masina)


# Dict

dictionar = {
   "culoare":"rosu",
   "roti":"4",
   "marca":"BMW",
   "specificatii":{
      "lungime":20,
      "latime":10,
      "inaltime":5
   }
}

dictionar2 = {
    'putere':125,
    'model':520,
    }

if dictionar.get('specificatii').get('inaltime') == 0:
    dictionar['specificati']['latime'] = dictionar2['putere']
    dictionar['culoare'] = dictionar2['putere']
    print(dictionar)
elif len(dictionar) >= 0:
    print('Am ajuns aici')




# print(dictionar.get('specificatii').get('latime'))
# print(len(dictionar))

# print(dictionar['roti'].replace(dictionar2))
# print(dictionar.get('roti').replace('4','6'))
# print(dictionar.update('roti').replace('4','6'))
# dictionar['roti'] = dictionar2
# print(dictionar)


# list = ['mere', 10, True, 2.51, 'pere', 66]
# list[2] = 'portocale'
#
# list2 = ['ananas', 98, 'cirese', 2.65]
#
# list2[1] = list[3]
#
# print(list2)