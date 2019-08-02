# -*- coding: utf-8 -*-

def ReadCompList():
    CompList=dict()
    AllComp=[]
    f = open("Compétences.tsv", 'r', encoding='utf8')
    lines=f.readlines()[1:]
    for line in lines:
        ls=line.split("\t")
        if len(ls[1])>1:
            CompList[ls[1]]=dict()
            Key0=ls[1]

        if len(ls[2])>1:
            if len(lsPrev[2])>1:
                CompList[Key0][lsPrev[2]]["Description"]=ls[6]
                if Key0=="Combat":
                    CompList[Key0][Key1]["Degat"]=ls[4]
                    CompList[Key0][Key1]["Portee"]=ls[5]

            CompList[Key0][ls[2]]=dict()
            Key1=ls[2]
        if len(ls[3])>1:
            CompList[Key0][Key1][ls[3]]=dict()
            Key2=ls[3]
            if Key0=="Combat":
                CompList[Key0][Key1][Key2]["Degat"]=ls[4]
                CompList[Key0][Key1][Key2]["Portee"]=ls[5]

            CompList[Key0][Key1][Key2]["Description"]=ls[6]
        lsPrev=ls.copy()
    return CompList

def FindCompInCompList(comp,complist):
    if "combat à" in comp or "combat avec" in comp:

        comp=comp.split(" : ")[1]
        
    for key0 in complist.keys():
        for key1 in complist[key0].keys():
            if comp in complist[key0][key1].keys():
                return key0,key1

    return False
