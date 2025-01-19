 # -*- coding: utf-8 -*-
import string, re,time,sys
from FichePerso import *
from Perso import Personnage
from Textes.ReadTextes import *
import Carac
from Lieux import Terminal, Table, TOilettes, Malle, Miroir
from Functions import *
# from kitchen.text.converters import getwriter
# UTF8Writer = getwriter('utf8')
# sys.stdout = UTF8Writer(sys.stdout)

Perso=Personnage()

if "-f" in sys.argv:
    Perso.print_speed = 1
elif "-ff" in sys.argv :
    Perso.print_speed =2
else :
    Perso.print_speed = 0

class QuFormatter(string.Formatter):
    def _quote(self, m):
        if not hasattr(self, 'quoted'):
            self.quoted = {}
        key = '__q__' + str(len(self.quoted))
        self.quoted[key] = m.group(2)
        return '{' + m.group(1) + key + m.group(3) + '}'

    def parse(self, format_string):
        return string.Formatter.parse(self,
            re.sub(r'{([^}`]*)`([^}`]*)`([^}]*)}', self._quote, format_string))

    def get_value(self, key, args, kwargs):
        if key.startswith('__q__'):
            key = self.quoted[key]
        return string.Formatter.get_value(self, key, args, kwargs)


delay_print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&%%%%@@@@@@@@@@@@@@%%&@@@@@@@@@@@@&%@@@@@@@@@@@@@@@@@@%&@@@@@@@@@@@@&%%@@@@@%%@@@@@@@@@&%@@@@@@@@@@&%%%%%%&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&, ,(%%(#@@@@@@@@@@@@*  .&@@@@@@@@@@@* %@@@@@@@@@@@@@@@@,  %@@@@@@@@@@@@# ,@@, ,@@@@@@@@@@* %@@@@@@@@@# *#%%%&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@. &@@@@@@@@@@@@@@@@@( /* ,@@@@@@@@@@@* %@@@@@@@@@@@@@@@* #,./@@@@@@@@@@@@&.  .(@@@@@@@@@@@* %@@@@@@@@@# *#%%%@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@&..@@,   ,@@@@@@@@@@&..&&* #@@@@@@@@@@* %@@@@@@@@@@@@@@% ,@# .&@@@@@@@@@@@@(  (@@@@@@@@@@@@* %@@@@@@@@@# .,,,*@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@* (@@@&.,@@@@@@@@@@, ,,,,. &@@@@@@@@@* %@@@@@@@@@@@@@&. ,,,. ,@@@@@@@@@@@* (#  #@@@@@@@@@@* %@@@@@@@@@# /&@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%,.    *@@@@@@@@@/ (@@@@& ,@@@@@@@@@*      #@@@@@@@@, %@@@@# /@@@@@@@@%..&@@&( *@@@@@@@@@* %@@@@@@@@@#      .@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@(                                                                                                                      (&@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@,                                                                                                                    .#&@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#                                                                                                                    *%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@,                 ,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&%#((/((#((/////////%%((##%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%*               *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(((##(//(/(((((///(//#%(##%@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%              (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%(((#(//(((((((((((((////(%###%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@/            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%##((((((((((##%&@@@@@@@@@(((#(/(((((((###((((((((///#%(#%&@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&.          (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#((/////////////////((#%@@(((((//((((#%%&&&&&&%((((((//####%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@(         #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#((//////****************///(((/(((((((#%&&&&&&@@&&&&%##(((/(%###&@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@.      .&@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#((///*********************//////((((#%&&&@@@@@@@@@@@&&%#(((//###%@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&%&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((///**************,******//////(((#%&&%%%&@&@@@@@@@@&&&%((///###%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#(////**********,,,,,****//////(((#%&&%#(////(&@@@@@@@@&&%(((/(#(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((////*********,,,,,****//////((#%&%#(/*******//(%@@@@@@&%((//(#(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%((////********,,,,,,***///*/(((#%%#(*,,,,,,,******/(#@@@&%(((/(#(%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((////*******,,,,****///*//(#%%%(*,,,,,,,,,,,,,,***//(#((((#(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(///***********,***//////(#%%(/,..,...,,,,,,,,*****///((((/(#(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#((///*************/////((#%#(*,..,....,,.,,,,****///////(((#((%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%((///**********///*///(%%#(*...........,,,,,**********///((#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((///*******//////((%%#*,,..........,,,,**************///((%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((/////***//////((#%#/,,..........,,,,*****,,**********///((%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#((////////////(#%%#/,,.,.......,,,,,******,,,,*********////(%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#(((////////((%%(**,,,,.,....,,,,,***,,,,,,,,,**********///((%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#(((/////((#%#/*,,,,,,....,,,,,***,,,,,,,,,,,,**********///(#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#(////((%%%#/*,,,,,,,,.,,,*****,,,,,,,,,,,,************///((%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((///(#%%#(***,,,,,,,,,,,****,*,,,,,,,,,,,,*****,,****////((#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(#///(#%%#(*****,,,,,,,,*******,,,,,,,,,,,,,***,,,****/////(((%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(((/(((#&%#(//******,,*************,,*********,,,,******/////((#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#(#(//(#&&&%#((////*******///*******************,,******/////((((#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(##((/(#&&@@@#((//////////******************,,*******///////(((#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%((#(/((#%&@@@@@@%##((/////////*************************///////((##%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&%(##//(((%&&@@@@@@@@#(((((((////////*************///////////((((##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.      #@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%#(##/(((##&&@@@@@@@@@@@@%####((((////////////****////////////((((##%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.        &@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%#(##((((##&&&@@@@@@@@@@@@@@@&%###((((((/////////////////////((####%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&,         ,@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%#(#(//((((#&&&&&&@@@&&&&&%@@@@@@@&%###(((((((((((((((((((((((###%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#            /@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#(%(///((((#%&&&&&&&&%##(((&@@@@@@@@&%%%###(((((((((((((((####%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*             #@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@%#(##////(((((((####((((((//((%@@@@@@@@@@@@&&%%############%%%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/               &@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%##(%#///(((((((((((((((/((##((#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(                ,@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%###(#%(/////((//(////((##(((%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  /@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#/***/,,,,,**,,******,,..,*(##((#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.                   #@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@,                                                                                                                        &@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@#.                                                                                                                        ,@@@@@@@@@@@@@@@@
@@@@@@@@@@@@%,                                                                                                                       ./@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""", perso= Perso, ts=0.0001)
delay_print("""

                                                                                                                 
Une planète pyramidale violette tourne autour de toi. Elle est d'abord loin et t'apparaît petite mais elle se rapproche doucement et inexorablement de toi. Elle devient de plus en plus grosse et tu n'en discernes maintenant plus très bien les bords. Tu commences alors à tomber en chute libre vers le sol.
Tu aperçois sur le sol une forme de fractale légèrement bleutée. Ta chute semble ne jamais finir. La fractale grossit néanmoins petit à petit. Tu vois maintenant en son centre une grande montagne pointue sur laquelle tu vas t'écraser. Tu es saisi d'une peur panique.
C'est à ce moment que tu te réveilles.


Alors que tu cherches à interpréter cet étrange cauchemar, une peur soudaine te saisit. Où es tu ? 
Où étais tu lorsque tu t'es endormi ? 
Où étais tu hier...                                                 
... la semaine dernière...                                         
... il y a 6 mois...                                           
... il y a 6 siècles ???                                
Ton esprit est très embrouillé. Tu n'as plus aucun souvenir.                                   
Tes sens s'activent néanmoins peu à peu.

""", perso= Perso)
if not Perso.print_speed == 0:
    time.sleep(2)
print("""De quel règne es-tu originaire ?""")
Races=RacesL()
RegneChoisie=False
while not RegneChoisie:
    print("\n Entre le nom d'un règne pour obtenir une description.")
    RegneTmp=Input(["Animal","Minéral","Végétal"])
    print(Races[RegneTmp+"Descr"]) #affiche la valeur du dictionnaire "Races" dont la clé est composée de ce que le joueur à entré + Descr. Exemple : MinéralDescr pour accéder au contenu voulu.
    print("Veux-tu choisir le règne {} ?".format(RegneTmp))
    if Input(["o","n"])=="o":
        Perso.Regne=RegneTmp
        RegneChoisie=True
    else:
        print("""De quel règne es-tu originaire ?\n""")

Perso.Regne = RegneTmp
Regne=Perso.Regne
print("""\n Quelle est ta race ?\n""")


global Race
RaceChoisie=False
while not RaceChoisie :
    list_races = list(Races[Regne].keys())
    list_races.remove("Description")
    print("""Les races existantes sont \n {}\n""".format(list_races))
    print("\n Entrer le nom de la race pour obtenir une description : \n")
    RaceTmp = Input(list_races)
    print("{}.".format(Races[Regne][RaceTmp]["Description"]))
    print("Bonus")
    for C in Races[Regne][RaceTmp]["Bonus"].keys():
        try:
            val=float(Races[Regne][RaceTmp]["Bonus"][C])
            if val>0:
                strL="+{}".format(val)
            else:
                strL="{}".format(val)
        except:
            strL=Races[Regne][RaceTmp]["Bonus"][C]
        print("{:<12} : {}".format(C,strL))
    print("Veux-tu choisir d'être un {}?".format(RaceTmp))
    if Input(["o","n"])=="o":
        Perso.RaceInfo=Races[Regne][RaceTmp]
        Perso.Race=RaceTmp
        RaceChoisie=True
    else:
        print("""\n Quelle est ta race ?\n""")
#if Regne = 

delay_print(Perso.RaceInfo["Intro"], perso= Perso)
if Perso.Race=="Corayy":
    print("\n")
    sys.exit()

if Regne=="Animal":
    Texte="des toilettes"
    Toilettes="Toilettes"
elif Regne=="Végétal":
    Texte="un cabanon de jardinage"
    Toilettes="Cabanon"
elif Regne=="Minéral":
    Toilettes="Sonde"
    Texte="une multi micro-sonde électronique tomographique"
delay_print("""Tu te trouves dans une pièce carrée d'environ cinq mètres par cinq. De l'ensemble du plafond se dégage une lumière parfaitement homogène et bleutée.  
Le lit sur lequel tu t'es réveillé est dans un coin de la pièce. A côté du lit, il y a une table Louis XV en acajou céleste. Il n'y a rien sur la table mais il y a deux tiroirs avec une poignée en marbre rose. A côté de la table, il y a un miroir. Au pied du lit, il y a une malle métallique.  Sur le mur opposé à la table, il y a un terminal numérique comprenant un écran et un casque synaptique. Dans le coin opposé il y a une porte. Enfin à droite de la porte il y a {}.\n""".format(Texte), perso= Perso)

if Regne=="Animal":
    print("""
________________________________________________________________
|                 ________         |            ||             |
|                  Miroir          |   Table    ||             |
|                                  |            ||             |
|                                  |____________||             |
|___                                             |    Lit      |
|   \                                            |             |
|    ) Toilettes                                 |             |
|___/                                            |             |
|                                                |             |
|                                                |             |
|                                                |_____________|
|                                                 ___________  |
|                                                 |         |  |
|                                                 |  Malle  |  |
|                                                 |_________|  |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|___                                                           |
|  /                                       Terminal            |
| / Porte                                   _______            |
|/                                         |       |           |
|__________________________________________|_______|___________|

""")
elif Regne=="Minéral":
    print("""
________________________________________________________________
|                 ________         |            ||             |
|                  Miroir          |   Table    ||             |
|                                  |            ||             |
|                                  |____________||             |
|___                                             |    Lit      |
|   |  Micro                                     |             |
|   |  Sonde                                     |             |
|___| électronique                               |             |
|                                                |             |
|                                                |             |
|                                                |_____________|
|                                                 ___________  |
|                                                 |         |  |
|                                                 |  Malle  |  |
|                                                 |_________|  |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|___                                                           |
|  /                                       Terminal            |
| / Porte                                   _______            |
|/                                         |       |           |
|__________________________________________|_______|___________|

""")
if Regne=="Végétal":
    print("""
________________________________________________________________
|                 ________         |            ||             |
|                  Miroir          |   Table    ||             |
|___________                       |            ||             |
|           \                      |____________||             |
|  cabanon  |                                    |    Lit      |
|    de     |                                    |             |
| jardinage |                                    |             |
|           |                                    |             |
|           |                                    |             |
|           |                                    |             |
|___________/                                    |_____________|
|                                                 ___________  |
|                                                 |         |  |
|                                                 |  Malle  |  |
|                                                 |_________|  |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|                                                              |
|___                                                           |
|  /                                       Terminal            |
| / Porte                                   _______            |
|/                                         |       |           |
|__________________________________________|_______|___________|

""")

if Regne == "Minéral":
    delay_print("Tu ressens un besoin pressant d'aller réactiver ta structure cristalline à la micro-sonde électronique.", perso= Perso)
elif Regne == "Animal":
    delay_print("Tu as très envie d'aller aux toilettes.", perso= Perso)
elif Regne == "Végétal":
    delay_print("Tes extremités organiques ont beaucoup trop poussé. Tu auras du mal à te mouvoir tant que tu n'auras pas pris soin de ta taille.", perso= Perso)
delay_print("Où souhaites-tu aller ?\n", perso= Perso)
#ListLieux=["Toilettes","Table","Terminal","Porte"]

ListLieux = [Toilettes, "Porte", "Table", "Terminal", "Malle", "Miroir"]
Completed=dict()
for entry in ListLieux:
    Completed[entry]=False

while not all(list(Completed.values())):
    Lieu = Input(ListLieux, perso=Perso, type="Perception")

    if ((not Completed[Toilettes]) and
        Lieu != Toilettes):
        if Regne == "Minéral":
            delay_print("Ton envie d'aller réactiver ta structure cristalline est vraiment trop pressante.", perso= Perso)
        elif Regne == "Végétal":
            delay_print("Ton besoin de taille est vraiment trop pressant.", perso= Perso)
        elif Regne == "Animal":
            delapy_print("Ton envie de te soulager est vraiment trop pressante.", perso= Perso)
        print("Où veux-tu aller?\n")
        continue

    delay_print("Tu te déplaces vers le (la) {}.".format(Lieu), perso=Perso, type="vitesse")
    if Completed[Lieu]:
        if Lieu == "Miroir":
            delay_print("Tu te regardes dans le mirroir. Tu n'as pas changé depuis tout à l'heure.", perso= Perso)
        else:
            print("Plus rien à découvrir ici.\n")
        print("Où souhaites-tu aller?\n")
        continue
    if Lieu== Toilettes :
        Perso.CaracBase=TOilettes(Regne,Perso)
        UpdateCarac(Perso)
        if Perso.Carac2["P2V"]<0:
            print("Tu n'as malheureusement pas assez de points de vie")
            delay_print("Tu te sens très faible. Ton prof de sport te disait souvent que tu étais de trop faible constitution. Il avait visiblement raison. Tu succombes à tes blessures.\n GAME OVER \n", perso= Perso)
            sys.exit()
        Completed[Toilettes]=True
    if Lieu=="Terminal":
        Terminal(Perso)
        Completed["Terminal"]=True

    if Lieu == "Miroir":
        Miroir(Perso)
        Completed["Miroir"] = True
    if Lieu=="Malle":
        Malle(Perso)
        Completed["Malle"]=True
        
    if Lieu=="Table":
        Info=Table(Perso)
        Perso.Descr=Info["Descr"]
        Perso.Age=Info["Age"]
        Perso.Nom=Info["Nom"]
        Perso.Descr=Info["Descr"]
        if Info!=None:
            Completed["Table"]=True
    if Lieu=="Porte":
        Completed["Porte"]=True
        if not all(list(Completed.values())):
            delay_print("""Tu t'approches de la porte. C'est une porte métallique avec une poignée en bois.\n""", perso= Perso, type = "Perception")
            print("""Veux-tu ouvrir la porte ?\n""")
            ouvrir=Input(["o","n"])            
            if ouvrir=="o":
                delay_print("""La porte est fermée de l'extérieur.\n""", perso= Perso)
            print("""Veux-tu toquer à la porte?\n""")
            ouvrir=Input(["o","n"])            
            if ouvrir=="o":
                delay_print("""Rien ne se passe.\n""", perso= Perso)
            print("""Veux-tu cogner fort dans la porte ?\n""")
            ouvrir=Input(["o","n"])
            iLoop=0
            TextDouleur="Rien ne se passe sauf que tu viens de te faire"
            while ouvrir=="o":
                delay_print(TextDouleur+" mal\n", perso= Perso)
                TextDouleur+=" très"
                try:
                    p2VLost=int(Perso.Carac["Force"]*0.1*min(10,iLoop+1))
                except:
                    p2VLost=int(50*0.1*min(10,iLoop+1))
                print("""Tu perds {} points de vie\n""".format(p2VLost))

                try:
                    Perso.Bonus["P2V"]-=p2VLost
                except:
                    Perso.Bonus=dict()
                    Perso.Bonus["P2V"]=-p2VLost

                UpdateCarac(Perso)
                try:
                    P2VLeft=Perso.Carac2["P2V"]
                    print("Il ne te reste plus que {} points de vie".format(P2VLeft))
                except :
                    P2VLeft=1
                if P2VLeft<=0:
                    delay_print("""Ce coup dans la porte est malheureusement la dernière action que tu peux entreprendre. Tu t'écroules par terre, mort. \nGAME OVER\n""", perso= Perso)
                    sys.exit()
                if iLoop==0:
                    delay_print("""En regardant attentivement la porte tu remarques qu'en dessous de la poignée est écrit en petites lettres : "connais toi toi-même"\n""", perso= Perso)
                print("""Veux-tu cogner encore plus fort dans la porte?\n""")
                ouvrir=Input(["o","n"])
                iLoop+=1


            Completed["Porte"]=False
        else:
            delay_print("""Tu t'approches de la porte.""", perso=Perso, type = "Vitesse")
            delay_print("""C'est une porte métallique avec une poignée en bois.\n""", perso= Perso, type= "Perception")
            print("""Veux-tu ouvrir la porte?\n""")
            ouvrir=Input(["o","n"])            
            if ouvrir=="o":
                print("C'est la fin du jeu. GAME OVER (enfin sauf si t'as beaucoup de chance) A FAIRE")

    if not Completed["Porte"]:
        print("Avant de continuer la création de personnage, veux tu imprimer ta fiche de personnage?")
        ppp=Input(["o","n"])
        
        if ppp=="o":
              PrintFichePerso(Perso)
        print("Où veux-tu aller?\n")

