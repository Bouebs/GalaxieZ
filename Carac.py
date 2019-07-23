# -*- coding: utf-8 -*-
import random
import numpy as np


def InitializeCarac(base):
    Carac=dict()
    
    for entry in ["Force","Endurence","Vitesse","Perception","Précision","Social","Intelligence","Sensibilité","Volonté"]:
        if base==None:
            Carac[entry]=None
        else:
            Carac[entry]=random.randint(0,base)
    return Carac


def InitializeBonusCarac(val=0):
    Bonus=dict()
    for entry in ["Force","Endurence","Vitesse","Perception","Précision","Social","Intelligence","Sensibilité","Volonté"]:
        Bonus[entry]=val
    return Bonus

def FuncUpStableDown(bmin,age,agemin,age1,age2,agemax):
    if age<age1:
        Val=bmin+(1-bmin)*(age-agemin)/(age1-agemin)
    elif age<age2:
        Val=1
    elif age<agemax:
        Val=1+(bmin-1)*(age-age2)/(agemax-age2)
    

    return Val


def BonusAge(age,agemin,agemax,age1=0,age2=0):
    if age1==0:
        age1=max(2*agemin,agemin+2)
    if age2==0:
        age2=0.7*agemax
    Bonus=dict()
    Bonus["Force"]=FuncUpStableDown(0.3,age,agemin,age1,age2,agemax)
    Bonus["Endurence"]=FuncUpStableDown(0.7,age,agemin,age1,age2,agemax)
    Bonus["Vitesse"]=FuncUpStableDown(0.7,age,agemin,(agemin+age1)/2,(age1+age2)/2,agemax)
    Bonus["Perception"]=FuncUpStableDown(0.3,age,agemin,agemin,(age1+age2)/2,agemax)
    Bonus["Précision"]=FuncUpStableDown(0.7,age,agemin,age1,age2,agemax)
    Bonus["Social"]=FuncUpStableDown(0.7,age,agemin,agemax,agemax,agemax)
    Bonus["Intelligence"]=FuncUpStableDown(0.8,age,agemin,age1,age2,agemax)
    Bonus["Volonté"]=1
    Bonus["Sensibilité"]=FuncUpStableDown(0.3,age,agemin,agemin,(age2+agemax)/2,agemax)
    Bonus["Expérience"]=np.sqrt(age)*10
    return Bonus

def CalculeCarac2(Perso,Equipement=None,XPRandom=0):
    C=Perso.Carac
    C2=dict()
    C2["P2V"]=(C["Force"]+C["Endurence"]+C["Volonté"])
    C2["Moral"]=(C["Perception"]+C["Intelligence"]+C["Volonté"])
    C2["Magie"]=(C["Perception"]+C["Intelligence"]+C["Sensibilité"])
    #Carac2["Réputation"]=NaN
    C2["Expérience"]=XPRandom+(C["Vitesse"]+C["Intelligence"]+C["Volonté"])*10
    #Carac2["Dégats"]=NaN
    return C2
