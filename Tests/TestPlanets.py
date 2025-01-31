import sys
import os

#Ajoute le dossier parent (GALAXIEZ) à sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Textes.ReadTextes import *
import random

def LoadPlanetes():
    f = my_open_file_in_Textes("Galaxie Z - Planètes.tsv")
    ListPlanetes = dict()
    for regne in ["Minéral", "Animal", "Végétal"]:
        ListPlanetes[regne] = dict()
    for line in f.readlines()[1:]:
        if len(line) < 4:
            continue
        ls = line.split("\t")
        if ls[4] == "o":
            ListPlanetes["Minéral"][ls[2]] = ls[3]
        if ls[5] == "o":
            ListPlanetes["Végétal"][ls[2]] = ls[3]
        if ls[6] == "o":
            ListPlanetes["Animal"][ls[2]] = ls[3]

    return ListPlanetes

planetes=LoadPlanetes()

print("La liste des planètes est la suivante : {}".format(planetes["Végétal"].keys()))