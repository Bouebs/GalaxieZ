import sys,time
from Carac import *
from _ast import If
import random
from Perso import Personnage

def delay_print(s, perso: Personnage, ts=0.04, type=None):
    if perso and perso.print_speed == 2:
        print(s)
        return

    if type in ["vitesse", "Vitesse"] and perso.Carac["Vitesse"]:
        
        v = perso.Carac["Vitesse"]
        print("vitesse = " + str(v))
        if v == 0:
            delay_print("Tu es beaucoup trop lent. Même l'éternité ne te suffirait pas à faire ce que tu viens d'entreprendre. Tu te demandes d'ailleurs pendant longtemps comment tu as pu accomplir autant de choses en étant aussi lent....\n")
            time.sleep(3)
            delay_print("Mais comment as tu d'ailleurs pu faire la moindre chose?\n")
            time.sleep(3)
            delay_print("C'est vraiment très surprenant.\n")
            time.sleep(4)
            delay_print("Tu te poses ces questions jusqu'au moment où tu meurs de soif.\n")
            time.sleep(1)
            print("GAME OVER")
            time.sleep(6)
            sys.exit()

        if  v < 20 :
            ts = 5 * (20. - int(v)) ** 3 / 19 / 100 + 0.04

    elif type in ["Perception, perception"] and Perso.Carac["Perception"] < 20:
        proba = float(Perso.Carac["Perception"]) / 20
        if Perso.Carac["Perception"] == 0:
            delay_print("Tu ne vois rien autour de toi. Il t'es impossible de te repérer. Tu moeurs lentement en te demandans comment tu as réussi à accomplir autant de choses jusqu'à présent sans rien voir ni sentir...")
            print("GAME OVER")
            time.sleep(6)
            sys.exit()
        for c in s:
            if random.random(1) < proba:
                caractere = c
            else:
                caractere = "#"
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(ts)
    elif perso and perso.print_speed == 1:
        print(s)
    else:
        for c in s:

            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(ts)


def Input(ListInputPossibles, perso=None, type=None):
    delay_print(str(ListInputPossibles), ts=0.01, perso=perso , type=type)

    rep= input() 
    while rep not in ListInputPossibles:
        print("Réponse non comprise")
        delay_print(ListInputPossibles, ts=0.01, perso=perso , type=type)
        print(ListInputPossibles)
        rep=input()
    return rep


def UpdateCarac(Perso):
    PAsDict=vars(Perso)
    if "CaracBase" in PAsDict.keys():
        Perso.Carac=dict()
        for C in Perso.CaracBase.keys():
            Perso.Carac[C]=Perso.CaracBase[C]
        try:
            for C in Perso.Bonus.keys():
                Perso.Carac[C]+=Perso.Bonus[C]
        except:
            Nothing=0
            
        try:
            BonusAg=BonusAge(Perso.Age,Perso.RaceInfo["AgeMin"],Perso.RaceInfo["AgeMax"])
            for C in BonusAg.keys():
                try:
                    Perso.Carac[C]=int(Perso.Carac[C]*BonusAg[C])
                except:
                    Error="Must be a Carac2"
        except:
            Error="Age pas encore défini"
                
        for C in Perso.RaceInfo["Bonus"].keys():
            if Perso.RaceInfo["Bonus"][C]=="Max 1":
                Perso.Carac[C]=1
            else:
                try:
                    Perso.Carac[C]+=Perso.RaceInfo["Bonus"][C]
                except:
                    Nothing = 0

        Perso.Carac2=CalculeCarac2(Perso)
        for C in Perso.Carac2.keys():
            try:
                Perso.Carac2[C]+=Perso.Bonus[C]
            except:
                Nothing = 0

        for C in Perso.Carac.keys():
            if Perso.Carac[C]<0:
                Perso.Carac[C]=0
