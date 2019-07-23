import sys,time
from Carac import *

def Input(ListInputPossibles):
    print(ListInputPossibles)

    rep= input() 
    while rep not in ListInputPossibles:
        print("Réponse non comprise")
        print("Les réponses possibles sont:")
        print(ListInputPossibles)
        rep=input()
    return rep


def delay_print(s, ts=0.04):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(ts)


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
