import unittest
from Perso import Personnage
from Functions import delay_print

class TestVitesse(unittest.TestCase):

    def test_Vitesse10(self):
        perso = Personnage()
        perso.Carac["Vitesse"]=10
        delay_print("Ce", perso= perso, type="Vitesse")

class TestPerception(unittest.TestCase):

    def test_perception5(self):
        perso = Personnage()
        perso.Carac["Perception"] = 10
        perso.print_speed = 1
        a = self.assertLogs(delay_print("Ceci est un long discours, qui fait plus de 50 caractères", perso=perso, type="Perception", ts = 0.0000001))

if __name__=="__main__" :
    unittest.main()
