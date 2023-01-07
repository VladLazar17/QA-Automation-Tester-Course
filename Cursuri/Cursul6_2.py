from Cursul6 import Floare

vaza = 0
trandafir = Floare('Rosie', 0)

def verifica_floarea_taiata(a):
    if trandafir.verifica_inaltimea() == True:
        a = a + 400
        print('Am adaugat apa in vaza')
    return a

vaza = verifica_floarea_taiata(vaza)
print(vaza)

# object = Masina()

# trandafir = Floare('Rosie', None)
# lalea = Floare('Galben', 5)
# trandafir.verifica_floare()
# lalea.verifica_inaltimea()

# lalea.verifica_floare()

