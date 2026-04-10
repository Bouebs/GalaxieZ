import sys
import os

#Ajoute le dossier parent (GALAXIEZ) à sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from Textes.ReadTextes import LoadPlanetes
import random

class TestLoadPlanetes(unittest.TestCase):
    def test_charge_fichier(self):
        planete_blob = LoadPlanetes()
        self.assertFalse(len(planete_blob)==0)

if __name__=="__main__" :
    unittest.main()
