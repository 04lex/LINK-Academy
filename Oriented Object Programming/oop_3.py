# Definesc clasa
# class Masina:
#     def __init__(self, marca:str, consum:float, kmparcursi:float, pret:int, rezervor = 0) -> None:
#         print("Constructorul clasei Masina a fost chemat")
        
#         # Initializare atribute clasa
#         self.marca = marca
#         self.consum = consum
#         self.kmparcursi = kmparcursi
#         self.pret = pret 
#         self.rezervor = rezervor
#         self.capacitate_rezervor = 100
#         self.bani_cheltuiti = 0
#         self.pret_benzina = 8

#     def __str__(self):
#         return f"{self.marca}-ul are un consum de {self.consum}, {self.kmparcursi} si un pret de {self.pret} negociabil. Are in rezervor {self.rezervor} litri."

#     def alimentare(self, benzina):
#         if self.capacitate_rezervor >= benzina + self.rezervor:
#             self.rezervor += benzina
#         else:
#             self.rezervor = self.capacitate_rezervor

#         self.bani_cheltuiti += benzina * self.pret_benzina

#     def parcurge_un_km(self):
#         # Inregistrare km parcursi
#         am_destul_in_rezervor = (self.consum / 100) < self.rezervor
#         if am_destul_in_rezervor:
#             self.kmparcursi += 1
#         # Consum benzina
#             self.rezervor -= self.consum / 100 # (km * l/100km)
#         else:
#             print("Pana prostului.")

#     def parcurgereKm(self, km):
#         for _ in range(km):
#             self.parcurge_un_km()
        


# # Creare obiect
# m1 = Masina("Dacia", 10, 50, 6, 20)
# m1.alimentare(10)
# print(m1)

# m1.parcurgereKm(100)
# print(m1)

# m1.parcurgereKm(50)
# print(m1)

# m1.parcurgereKm(500)
# print(m1)




# m2 = Masina("BMW", 15, 100, 20)
# print(m2)

# m2.alimentare(8)
# print(m2)

# m2.alimentare(800)
# print(m2)




# class Facultate:
#     def __init__(self, denumire:str, adresa:str):
#         self.denumire = denumire
#         self.adresa = adresa

#     def __str__(self):
#         return f'Facultatea {self.denumire} de la {self.adresa}'


# class Student:
#     # Variabila STATICA
#     VARSTA_MINIMA = 16
#     def __init__(self, nume:str, varsta:int, facultate:Facultate):
#         # Variabila publica
#         self.nume = nume
#         # Variabila interna
#         self._varsta = varsta
#         self.facultate = facultate
#         # Variabila privata
#         self.__note = []

#         # Functie setter pentru varsta
#     def setVarsta(self, noua_varsta):
#         if not isinstance(noua_varsta, int):
#             return
#         elif noua_varsta < Student.VARSTA_MINIMA:
#             return
#         else:
#             self._varsta = noua_varsta

#         # Functie getter pentru varsta
#     def getVarsta(self):
#         return "Major" if self._varsta > 10 else "Minor"

#     def getNote(self):
#         return tuple(self.__note)

#     def setNote(self, *noteNoi):
#         for nota in noteNoi:
#             if isinstance(nota, int) and nota in range (1, 11):
#                 self.__note.append(nota)


# Student.VARSTA_MINIMA = 30
# print(Student.VARSTA_MINIMA)



# medicina = Facultate("Carol Davila", "Pe la Eroilor")
# print(medicina)


# stud = Student("Ion Pop", 20, medicina)
# stud.setNote(9, 8)
# stud.setNote(7)
# print(stud.getNote())

# print(stud.note)
# stud.note.append(10)
# print(stud.note)

# stud.note.append(10)
# print(stud.note)

# stud.note.append(9)
# print(stud.note)

# print(stud.facultate.denumire)

# studenta = Student("Ioana Popa", 20, medicina)
# print(studenta.facultate.denumire)

# studenta.setVarsta('iuiuiu')
# print(studenta.getVarsta())



















# eu
 
# class STBCard:
#     def __init__(self, nume:str = None, calatorii:int = 0, credit:int = 0):
#         self.nume = nume
#         self.calatorii = calatorii
#         self.credit = credit

#     def balantaCredit(self):
#         if self.credit > 0:
#             return f'Credit: {self.credit}\nCalatorii: {self.calatorii}'
#         else:
#             return f"Reincarca cartela, credit {self.credit}, calatorii {self.calatorii}"

#     def showName(self):
#         if isinstance(self.nume, str):
#             return f'Nume: {self.nume}'
#         else:
#             print("Nume: Nenominal")

    

# card1 = STBCard('Alexandru', 1, 3)
# print(card1.balantaCredit())

# print(card1.showName())

# print('------------')

# card2 = STBCard(0, 0)
# print(card2.showName())
# print(card2.balantaCredit())








# silviu

class STBCard:
    COST_CALATORIE = 3

    def __init__(self, nume:str = "Nenominal", calatorii:int = 0, credit:int = 0):

        self.nume = nume
        self.calatorii = calatorii
        self.credit = credit
    def __str__(self):
        return f'Cardul lui {self.nume} are {self.calatorii} calatorii si {self.credit} lei.'

    def reincarcaCredit(self, bani):
        self.credit += bani

    def reincarcaCalatorii(self, calatorii):
        self.calatorii += calatorii

    def validareCalatorie(self):
        if self.calatorii > 0:
            self.calatorii -= 1
        elif self.credit > STBCard.COST_CALATORIE:
            self.credit -= STBCard.COST_CALATORIE
        else:
            print("Credit insuficient")


card1 = STBCard('Juan', 0, 0)
print(card1.calatorii)
card1.reincarcaCalatorii(2)
card1.reincarcaCredit(5)
print(card1)

card1.validareCalatorie()
print(card1)
card1.validareCalatorie()
print(card1)
card1.validareCalatorie()
print(card1)
card1.validareCalatorie()
print(card1)





# card2 = STBCard(0, 0)
# print(card2.nume)

