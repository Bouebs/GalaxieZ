import unittest
from Functions import delay_print
from Perso import Personnage

Perso = Personnage()

Perso.Carac = dict()
Perso.Carac["Vitesse"] = 15

for vitesse in [20, 15, 10, 5, 0]:
    Perso.Carac["Vitesse"] = vitesse
    delay_print("{} de vitesse".format(vitesse), perso=Perso, type="vitesse")
