import sys
import os

#Ajoute le dossier parent (GALAXIEZ) à sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Textes.ReadTextes import *
import random

EndL=EndList()
print("Tu parviens à ouvrir la porte, alors que la liberté d'un monde immense s'ouvre à toi tu sens qu'il s'agit d'un jour particulier. {}".format(EndL[random.randint(0,len(EndL))]))