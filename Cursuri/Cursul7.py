# numar = 3
#
# try:
#     assert numar % 2 == 0, 'pacat'
#
# except AssertionError as e:
#     print(e)


# def masina():
#     try:
#         numar_roti = int(input('Introdu numarul de roti: ' ))
#     except ValueError:
#         print('Numarul nu este de timp integer')
#     culoare = None
#     try:
#         return numar_roti
#     except UnboundLocalError:
#         print('Numar_roti este gol')
# masina()

# try:
#     int(roti) = masina()
# except


class om():
    def __init__(self, inaltime, greutate, culoare_ochi):
        self.inaltime = inaltime
        self.greutate = greutate
        self.culoare_ochi = culoare_ochi


class elev(om):
    def __init__(self, inaltime, greutate, culoare_ochi):
        super().__init__(inaltime, greutate, culoare_ochi)

# class om:
#     def __init__(self, inaltime, greutate, culoare_ochi):
#         self.inaltime = inaltime
#         self.greutate = greutate
#         self.culoare_ochi = culoare_ochi
#
#
# class elev(om):
#     def __init__(self, inaltime, greutate, culoare_ochi, clasa):
#         super().__init__(inaltime, greutate, culoare_ochi)
#         self.clasa = clasa
#
# class elev_absolvent(elev):
#     def __init__(self):
#
#
# class Angajat(om):
#     nume = None
#     prenume = None
#     salariu = None
#
#     def __init__(self, a, b, c):
#         self.nume = a
#         self.prenume = b
#         self.salariu = c
#
#     def descrie(self):
#         print(f'Numele angajatului este: {self.nume} ')
#         print(f'Prenumele angajatului este: {self.prenume}')
#         print(f'Are salariul {self.salariu}')
#
#     def nume_complet(self):
#         print(self.nume + ' ' + self.prenume)
#
#     def salariu_lunar(self):
#         print(f'salariul lunar este de

# -------------------------------------------------Abstractizare
# from abc import abstractmethod
#
#
# class figura_geometrica():
#     @abstractmethod
#     def defineste_forma(self):
#         raise NotImplementedError
#
#     @abstractmethod
#     def stabileste_perimetrul(self):
#         raise NotImplementedError
#
#
# class patrat(figura_geometrica):
#     def defineste_forma(self):
#         numar_laturi = input('Introdu numarul laturilor: ')
#
#
# patrat1 = patrat()
# patrat1.defineste_forma()
