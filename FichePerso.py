# -*- coding: utf-8 -*-
from Carac import *
from Competences import *
from Functions import *
import string
class PartialFormatter(string.Formatter):
    def __init__(self, missing=' ', bad_fmt=' '):
        self.missing, self.bad_fmt=missing, bad_fmt

    def get_field(self, field_name, args, kwargs):
        # Handle a key not found
        try:
            val=super(PartialFormatter, self).get_field(field_name, args, kwargs)
            # Python 3, 'super().get_field(field_name, args, kwargs)' works
        except (KeyError, AttributeError):
            val=None,field_name 
        return val 

    def format_field(self, value, spec):
        # handle an invalid format
        #if value==None: return self.missing
        if value==None: value=" "
        try:
            return super(PartialFormatter, self).format_field(value, spec)
        except ValueError:
            if self.bad_fmt is not None: return self.bad_fmt   
            else: raise
fmt=PartialFormatter()
def xstr(s):
    return '' if s is None else str(s)

def PrintFichePerso(Perso):
    UpdateCarac(Perso)
    PersoAsDict=vars(Perso)

        

    print("""########################################################################################################
|_______________________________________FICHE DE PERSONNAGE____________________________________________|
|                                                                                                      |""")
    print(fmt.format("""| IDENTITE_____________________________________________________________________________________________|"""))


    ListIdType=[["Nom","Nom"],["Age","Age"],["Planete","Planète d'origine"],["Sexe","SexeType"],["Regne","Règne"],["Race","Race"]]
    First=True
    iLine = 0
    for id in ListIdType:

        if id[0] in PersoAsDict.keys():
            if id[0]=="Sexe":
                id[1]=Perso.SexeType
            if First:

                strL = "| {:39s}".format(id[1] + " : " + str(PersoAsDict[id[0]]))
                First=False
                continue
            else:

                strL = strL + " {:33s}".format(id[1] + " : " + str(PersoAsDict[id[0]]))
                First = True
                if Perso.Mirroir:
                    strL += "|{:27s}|".format(' ')
                else :
                    strL += " {:27s}|".format(' ')
                print(strL)
                iLine += 1

    if not First:
        strL = strL + " {:33s}".format(" ")
        if Perso.Mirroir:
            strL += "|{:27s}|".format(' ')
        else :
            strL += " {:27s}|".format(' ')

        print(strL)
        iLine += 1
        First=True
    if Perso.Mirroir :
        while iLine < 14 :
            if iLine == 5:
                print("| {:73s}|{:27s}|".format("", "COLLEZ"))
            elif iLine == 7:
                print("| {:73s}|{:27s}|".format("", "VOTRE PORTRAIT"))
            elif iLine == 9:
                print("| {:73s}|{:27s}|".format("", "ICI"))
            else:
                print("| {:73s}|{:27s}|".format("", ""))
            iLine += 1
    # if "Nom" in PersoAsDict.keys():
    #     print(fmt.format("| Nom : {Nom:50s} Planète d'origine : {Planete:22s} |",**PersoAsDict))
    # print(fmt.format("| Règne : {Regne:25s}   Race : {Race:18s}                                       |",**PersoAsDict))
    
    # if "Age" in PersoAsDict.keys():
    #     StrAge="| Age : {:10s} ".format(str(PersoAsDict["Age"]))
    # else:
    #     StrAge="|       {:10s} ".format(" ")
    # if "Sexe" in PersoAsDict.keys():
    #     StrSex="                   {:12s} : {:13s}                                    |".format(Perso.SexeType,Perso.Sexe)
    # else:
    #     StrSex="                   {:12s}   {:13s}                                    |".format(" ", " ")
    # if "Age" in PersoAsDict.keys() or "Sexe" in PersoAsDict.keys():
    #     print(StrAge+StrSex)

    if not Perso.Mirroir:
        print("|                                                                                                      |")
    if "Descr" in PersoAsDict.keys():
        print(fmt.format("""| BIOGRAPHIE __________________________________________________________________________________________|"""))
        istr=0
        strL=""
        prevBlank=False
        for sL in Perso.Descr:
            if istr==0:
                strL="| "+sL
                istr+=1
            elif istr==99:
                if prevBlank :
                    strL+="  |"
                    print(strL)
                    strL="| "+sL
                    istr=1

                elif sL==" " :
                    strL+=sL+" |"
                    print(strL)
                    strL=""
                    istr=0
                else :
                    strL+="- |"
                    print(strL)
                    strL="| "+sL
                    istr=1

            else:
                if sL==" ":
                    prevBlank=True
                else:
                    prevBlank=False

                strL+=sL
                istr+=1

        while istr<100:
            strL+=" "
            istr+=1
        strL+=" |"
        print(strL)
        print("|                                                                                                      |")
    if "Carac" in PersoAsDict.keys():
        print(fmt.format("""| CARACTERISTIQUES  ___________________________________________________________________________________|"""))
        ipos=0
        for c in Perso.Carac.keys():
            value=Perso.Carac[c]
            if ipos==0:
                strL="| {:25s}".format(c+" : "+str(value))
                ipos+=1
            elif ipos<3:
                strL+="{:25s}".format(c+" : "+str(value))
                ipos+=1
            else :
                strL+="{:25s} |".format(c+" : "+str(value))
                print(strL)
                ipos=0
                strL=""
            
        if ipos!=0:
            for ii in range(ipos,4):
                strL+="{:25s}".format(" ")
            strL+=" |".format(" ")
            print(strL)

        print("|                                                                                                      |")
        ipos=0
        
        Carac2=Perso.Carac2
        for c in Carac2:
            value=Carac2[c]
            if ipos==0:
                strL="| {:25s}".format(c+" : "+str(value))
                ipos+=1
            elif ipos<3:
                strL+="{:25s}".format(c+" : "+str(value))
                ipos+=1
            else :
                strL+="{:25s} |".format(c+" : "+str(value))
                print(strL)
                ipos=0
                strL=""
            
        if ipos!=0:
            for ii in range(ipos,4):
                strL+="{:25s}".format(" ")
            strL+=" |".format(" ")
            print(strL)

        print("|                                                                                                      |")

        
    if "Comp" in PersoAsDict.keys():
        print(fmt.format("""| COMPETENCES _________________________________________________________________________________________|"""))
        ListComp=dict()
        AllCompList=ReadCompList()
        
        for key0 in AllCompList.keys():
            print("| {:^99s}  |".format(key0," "))
            ipos=0
            for key1 in AllCompList[key0].keys():
                for compCheck in AllCompList[key0][key1].keys():
                    if compCheck in Perso.Comp.keys():
                        if key1=="langues" or key1=="mécanique":
                            strLL="{:33s}{:7s}".format(key1+" "+compCheck," niv "+str(Perso.Comp[compCheck]))
                        else:
                            strLL="{:33s}{:7s}".format(compCheck," niv "+str(Perso.Comp[compCheck]))


                        if ipos==0:
                            strL="| {:60s}".format(strLL)
                            ipos+=1
                        else :
                            strL+="{:40s} |".format(strLL)
                            print(strL)
                            ipos=0
            
                            strL=""

            if ipos!=0:
                for ii in range(ipos,2):
                    strL+="{:40s}".format(" ")
                strL+=" |".format(" ")
                print(strL)


    print("|______________________________________________________________________________________________________|")
