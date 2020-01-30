import unittest
from Perso import Personnage
from Functions import delay_print

class TestVitesse(unittest.TestCase):

    def test_Vitesse10(self):
        perso = Personnage()
        perso.Carac["Vitesse"]=10
        delay_print("Ceci doit prendre plus de 20 secondes", perso= perso, type="Vitesse")


if __name__=="__main__" :
    unittest.main()
