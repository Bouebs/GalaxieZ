import sys
from FichePerso import *
from Perso import *
from Lieux  import *
from Competences  import *
from Races import *
from Functions import *
import random,Carac









Perso=Personnage()
AllCompList=ReadCompList()

Perso.Comp=dict()
for key0 in AllCompList.keys():

    ipos=0
    for key1 in AllCompList[key0].keys():
        for compCheck in AllCompList[key0][key1].keys():
            tt=random.randrange(100)
            if tt<15:
                Perso.Comp[compCheck]=2


Races=RacesL()
Perso.RaceInfo=Races["Minéral"]["Crystallim"]
Perso.Carac=InitializeCarac(0)
Perso.Nom="Test"
Perso.Race="Crystallim"
Perso.Regne="Minéral"
Perso.Age=2
Perso.CaracBase=Carac.InitializeCarac(100)
UpdateCarac(Perso)
Perso.Mirroir = False
Perso.Sexe="Masculin"
Perso.SexeType="Sex"
#Perso.Carac=TOilettes("Mineral")
Perso.Descr="""Les Crystallim sont des cristaux conscients. Leurs mouvements sont étonnament rapides étant donné leur mode de déplacement par croissance crystalline. Les Crystallims sont assez fragiles mais ont pour particularité de partager un esprit commun avec leurs congénères. Les spécialistes humains appellent cela la résonnance, les Crystallims semblent capables de vibrer sur une fréquence commune qui leur permet de se mettre en empathie. Dans cet état tous les crystallims présents dans la pièce agissent comme une seule entité consciente. Lors des guerres du Septant l'emporium scientifique Paragytt avait essayé d'inhiber cette capacité par des brouilleurs mais cela a été un échec qui leur a couté l'annihilation. Les Crystallim ont une durée de vie très courte, ce qui est souvent ignoré des autres races dans la mesure où ils croissent les uns à partir des autres. Il est très difficile de distinguer un individu d'un autre. Les Crystallims n'ont que très peu d'affinités avec les fluctuations magiques."""



PrintFichePerso(Perso)

