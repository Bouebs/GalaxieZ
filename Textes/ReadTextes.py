# -*- coding: utf-8 -*-
import io


def SexeL():
    Sexes = dict()
    f = open("Textes/Galaxie Z - Sexes.tsv", 'r', encoding='utf8')
    lines = f.readlines()
    for line in lines[1:]:
        ls = line.split("\t")
        Sexes[ls[1]] = ls[2]

    return Sexes


def LoadFins():
    f = open("Textes/Galaxie Z - {}.tsv".format(Regne), 'r', encoding='utf8')
    f = open("Textes/Galaxie Z - Fins aléatoires 2078.tsv", encoding="utf-8")
    ListFins = []
    for line in f.readlines()[1:]:
        fin = line.split("\t")[1]
        if len(fin) > 3:
            ListFins.append(fin)

    return ListFins


def LoadPlanetes():
    f = open("Textes/Galaxie Z - Planètes.tsv", encoding="utf-8")
    ListPlanetes = dict()
    for regne in ["Minéral", "Animal", "Végétal"]:
        ListPlanetes[regne] = dict()
    for line in f.readlines()[1:]:
        if len(line) < 4:
            continue
        print(line)
        ls = line.split("\t")
        if ls[4] == "o":
            ListPlanetes["Minéral"][ls[2]] = ls[3]
        if ls[5] == "o":
            ListPlanetes["Végétal"][ls[2]] = ls[3]
        if ls[6] == "o":
            ListPlanetes["Animal"][ls[2]] = ls[3]

    return ListPlanetes


def Inventaire():
    f = open('Textes/Galaxie Z - Inventaire.tsv', encoding="utf-8")
    ListObj = []
    for line in f.readlines()[46:]:
        ls = line.split("\t")
        try:
            Obj = dict([["ValMax", int(ls[1].split()[-1])], ["Type", ls[2]], ["Nom", ls[3]], ["Matériau", ls[4]], ["Description", ls[5]], ["Poids", float(ls[6])]])
        except:
            print("ATTENTION PROBLEM DANS Inventaire.py")
            print(ls)
        if Obj["Nom"] != "Nef Ngometek" and Obj["Nom"] != "Perce-temps":
            ListObj.append(Obj)
            if len(ListObj) > 1:
                if ListObj[-1]["ValMax"] <= ListObj[-2]["ValMax"]:
                    print("Il y a un problème dans la liste d'objet sur les valeurs pour le tirage aléatoire")

    return ListObj


def ReadCompList():
    CompList = dict()
    AllComp = []
    f = open("Textes/Compétences.tsv", 'r', encoding='utf8')
    lines = f.readlines()[1:]
    for line in lines:
        ls = line.split("\t")
        if len(ls[1]) > 1:
            CompList[ls[1]] = dict()
            Key0 = ls[1]

        if len(ls[2]) > 1:
            if len(lsPrev[2]) > 1:
                CompList[Key0][lsPrev[2]]["Description"] = ls[6]
                if Key0 == "Combat":
                    CompList[Key0][Key1]["Degat"] = ls[4]
                    CompList[Key0][Key1]["Portee"] = ls[5]

            CompList[Key0][ls[2]] = dict()
            Key1 = ls[2]
        if len(ls[3]) > 1:
            CompList[Key0][Key1][ls[3]] = dict()
            Key2 = ls[3]
            if Key0 == "Combat":
                CompList[Key0][Key1][Key2]["Degat"] = ls[4]
                CompList[Key0][Key1][Key2]["Portee"] = ls[5]

            CompList[Key0][Key1][Key2]["Description"] = ls[6]
        lsPrev = ls.copy()
    return CompList


def FindCompInCompList(comp, complist):
    if "combat à" in comp or "combat avec" in comp:

        comp = comp.split(" : ")[1]

    for key0 in complist.keys():
        for key1 in complist[key0].keys():
            if comp in complist[key0][key1].keys():
                return key0, key1

    return False


def ExcuseL():
    Ex = []
    f = open("Textes/Galaxie Z - Excuses.tsv", 'r', encoding='utf8')
    lines = f.readlines()
    f.close()
    for line in lines[1:]:
        Ex.append(line)

    return Ex


def GetListMetiers():
    f = open("Textes/Métiers.tsv", 'r', encoding='utf8')
    lines = f.readlines()
    Metiers = dict()
    for line in lines[1:]:
        ls = line.split("\t")
        if len(ls[0]) > 1:
            Key0 = ls[0]
            Metiers[Key0] = dict()
            Metiers[Key0]["Descr"] = ls[2]
            Metiers[Key0]["Comp"] = [ls[1]]
        else:
            Metiers[Key0]["Comp"].append(ls[1])
    return Metiers


def RacesL():
    Races = dict()

    Regne = "Minéral"

    f = open("Textes/Galaxie Z - {}.tsv".format(Regne), 'r', encoding='utf8')

    lines = f.readlines()

    Races[Regne] = dict()

    Races["MinéralDescr"] = Races[Regne]["Description"] = lines[1].split("\t")[3]
    for line in lines[2:]:
        if len(line) < 20:
            break
        ls = line.split("\t")
        RaceL = ls[2].split()[1]
        Races[Regne][RaceL] = dict()

        Races[Regne][RaceL]["Description"] = ls[3]
        Races[Regne][RaceL]["SexeType"] = ls[4]
        if ls[4] != "non":
            Races[Regne][RaceL]["Sexe"] = []
            valsL = ls[5].split()
            for v in valsL:
                if v == "m":
                    Races[Regne][RaceL]["Sexe"].append("masculin")
                elif v == "f":
                    Races[Regne][RaceL]["Sexe"].append("feminin")
                else:
                    Races[Regne][RaceL]["Sexe"].append(v)
        Races[Regne][RaceL]["Intro"] = ls[6]
        Races[Regne][RaceL]["AgeMin"] = int(ls[7])
        Races[Regne][RaceL]["AgeMax"] = int(ls[8])
        Races[Regne][RaceL]["Bonus"] = dict()

        for Bonus in ls[9:]:
            if len(Bonus) > 2:
                BS = Bonus.split()
                if "Max" in BS[1]:
                    Races[Regne][RaceL]["Bonus"][BS[0]] = "Max 1"
                else:
                    Races[Regne][RaceL]["Bonus"][BS[0]] = int(BS[1])

    return Races
