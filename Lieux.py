# -*- coding: utf-8 -*-
from Functions import *
from Competences import *
import Carac,sys
import random
import Metier
import SexeList
import ExcuseList


def Terminal(P):
    delay_print("""Tu t'approche du terminal multimodal. Dès que tu le touche, celui-ci s'active et une voix dit : "identification de l'individu". Après un très bref délai, la voix reprend : "votre numéro pôle emploi est le numéro Z{}.
    \n""".format(random.randint(0,1000000000)))        
    CompList=ReadCompList()
    print("Quel est ton métier?")
    print("Choisir un métier te donne un niveau 2 (sur un maximum de 10) pour 10 compétences") 
    Metiers=Metier.GetListMetiers()
    MetierChoisie=False
    while not MetierChoisie:
        print("\n Entrer le nom d'un métier pour obtenir une description de ce métier ainsi que pour connaître les compétences associées.")
        MetierTmp=Input(list(Metiers.keys()))
        DescrL=Metiers[MetierTmp]["Descr"]
        if len(DescrL)<2:
            DescrL="Comment ça tu ne sais pas ce qu'est un {}? Soit t'es un boulet, ou alors peut-être que cette description manque car {}.".format(MetierTmp,ExcuseL[random.randint(0,len(ExcuseL))])


        print("Description : {}".format(DescrL))
        print("Compétences associées : {}\n".format(list(Metiers[MetierTmp]["Comp"])))
        print("Veux tu choisir d'être un {}".format(MetierTmp))
        if Input(["o","n"])=="o":
            P.Metier=MetierTmp
            MetierChoisie=True
            P.Comp=dict()
            for Comp in Metiers[MetierTmp]["Comp"]:
                P.Comp[Comp]=2


    PointsLeft=16
    print("""Tu peux maintenant répartir {} point comme tu le souhaite.""".format(PointsLeft))

    while PointsLeft!=0:
        print("Quel domaine de compétence veux tu améliorer")
        Key0=Input(list(CompList.keys()))
        if Key0 == "Combat":
            Key0Text= ""
        else:
            Key0Text= Key0
        while PointsLeft!=0:
            print("Quel sous domaine de compétence veux tu améliorer?")
            Key1=Input(list(CompList[Key0].keys()))
            while PointsLeft!=0:
                print("Dans le domaine {}, dans le sous domaine {}, les compétences sont {}".format(Key0,Key1,CompList[Key0][Key1].keys()))
                print("Entrer un compétence pour avoir un descriptif")
                CompL=Input(list(CompList[Key0][Key1].keys()))
                if len(CompList[Key0][Key1][CompL]["Description"])<5:
                    Descr="""Comment ça, tu ne sais pas ce qu'est un(e)"{}"? Soit t'es un boulet, soit les développeur n'ont pas bien fini ce jeu.""".format(CompL)
                else:
                    Descr=CompList[Key0][Key1][CompL]["Description"]
                    
                if "Degat" in CompList[Key0][Key1][CompL].keys():
                    print("Description : {}\n Dégât de base : {}\n Portée maximal en mètres : {}".format(Descr,CompList[Key0][Key1][CompL]["Degat"],CompList[Key0][Key1][CompL]["Portee"]))
                else:
                    print("Description : {}\n".format(Descr))
                    
                print("Veux tu développer cette compétence?")
                if Input(["o","n"])=="o":
                    print("Combien de points veux tu ajouter? (il te reste {} points à répartir)".format(PointsLeft))
                    pL=0
                    while not pL:
                        try:
                            pL = int(input())
                            break
                        except:
                            print("Tu dois entrer un nombre entier")

                    if CompL in P.Comp.keys():
                        pppp=P.Comp[CompL]
                    else :
                        pppp=0
                    if pL +pppp> 10:
                        print("Tu ne peux pas avoir plus de 10 points dans une compétence")
                    elif pL>PointsLeft:
                        print("Tu n'as plus autant de points à répartir")

                    else:
                        if CompL in P.Comp.keys():
                            P.Comp[CompL]+=pL
                        else:
                            P.Comp[CompL]=pL
                        PointsLeft-=pL
                        if PointsLeft==0:
                            break 
                print("Veux tu continuer d'améliorer tes compétences dans le même sous domaine ({})?".format(Key1))
                if Input(["o","n"])=="n":
                    break
            if PointsLeft==0:
                break 

            print("Veux tu continuer d'améliorer tes compétences dans le même domaine ({})?".format(Key0))    
            if Input(["o","n"])=="n":
                break
    
def Table(Perso):

    Info=None
    Rep="lll"

    while Rep!="p":
        print("""Veux tu ouvrir le tiroir de gauche (g), le tiroir de droite (d), ou partir (p)""")
        Rep=Input(["g","d","p"])
        
        if Rep=="g":
            delay_print("""Tu ouvre le tiroir de gauche mais celui ci est vide.\n""")
        elif Rep=="d":
            if Info!=None:
                delay_print("""Tu ouvre le tiroir de droite mais il n'y a plus rien dedans.\n""")
                continue
            delay_print("""Tu ouvre le tiroir de droite. A l'interieur, tu trouve un pièce d'identité numérique.""")
            Info=dict()
            Info["Nom"]="111111111111111111111111111111111111111111111111111111111111"
            while len(Info["Nom"])>15:
                print("Choisis ton nom\n")
                Info["Nom"]=input()
                if len(Info["Nom"])>15:
                    print(" Ce nom est trop long\n")
            age=0
            while not age:
                try:
                    age = int(input("Choisis ton âge en années\n"))
                    break
                except:
                    print("L'age doit être un nombre entier.")

            Info["Age"]=age
            if Info["Age"]>Perso.RaceInfo['AgeMax']:
                delay_print("Tu te sens très vieux d'un seul coup. Après tout {} ans est un très bel âge pour un {}. Tu t'effondre mort.\nGAME OVER\n".format(age,Perso.Race))
                sys.exit()
            if Info["Age"]<Perso.RaceInfo['AgeMin']:
                delay_print("Certains mystères ne pourront jamais être compris. Comment est ce qu'un {} de seulement {} ans a pu se retrouver ici sans aide? Tu pleure pendant des heures comme un bébé en espérant vainement que quelqu'un vienne s'occuper de toi.\nGAME OVER\n".format(Perso.Race,age))
                sys.exit()
            print("""A FAIRE!!!!! Ajouter choix de la planète de naissance""")

            delay_print("""En dessous de la pièce d'identité, il y a un carnet de note. En l'ouvrant tu découvre que c'est un journal intime\n""")
            Descr="eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
            lenmax=100
            while len(Descr)>lenmax:
                print("""Ecris un texte présentant ton personnage\n""")
                Descr=input()
                if len(Descr)>lenmax:
                    print("La description est trop longue (maximum {} caractères)\n".format(lenmax))
            delay_print("Il n'y a rien d'autre dans le tiroir de droite\n")
            Info["Descr"]=Descr


    return Info

def TOilettes(Regne,Perso):
    ExcuseL=ExcuseList.ExcuseL()

    SexeL=SexeList.SexeL()
    if Regne=="Animal":
        delay_print("Une envie pressante te pousse à aller visiter les toilettes.\n")
        print("Quel est ton sexe?\n")
        Sexe=Input(["Masculin","Feminin"])

        delay_print("""Tu te soulage... psssssssssss
                 ssssssssssssss

    ssss
sss
floq floq floq.
""")
        delay_print("""Une voix synthétique venue de nulle part dit: "analyse d'urine en cours... détermination des capacités."\n Un écran jusqu'alors invisible s'allume alors sur le mur derrière les toilettes.\n""")

    elif Regne=="Végétal":
        delay_print("""Comme tes membres ont poussé pendant ton sommeil, tu décides d'aller te faire une petite taille dans le cabanon de jardinage. Un séquateur te permet de te soulager... tchac tchic


tchac tchac

tchic tchic
Alors que tu jettes tes rebus dans le composteur, une voix synhétique venue de nulle part dit: "analyse génétique en cours... détermination des capacités."\n Un écran multi-sensoriel qui était jusqu'alors invisible s'allume alors sur un mur du cabanon.\n""")

    elif Regne=="Minéral":
        
        delay_print("""Tu décides d'aller vérifier ton état de santé à l'aide de la micro-sonde électronique tomographique. C'est un modèle dernier cri VEOLIA xd-spx667. Dès que tu t'approche suffisamment de la machine, celle ci se met en route. Une voix synhétique venue de nulle part dit: "analyse en cours veuillez patientez."\n Après quelques secondes d'attente un écran multi-sensoriel qui était jusqu'alors invisible s'allume face à toi.\n""")

    if Regne!="Animal":
        if Perso.RaceInfo["SexeType"]!="non":
            SexeChoisi=False
            
            while not SexeChoisi :

                print("Quel(le) est ton (ta) {}?".format(Perso.RaceInfo["SexeType"]))
                print("\n Entrer le nom d'un (d'une) {} pour obtenir une description\n".format(Perso.RaceInfo["SexeType"]))
                SexeTmp=Input(Perso.RaceInfo["Sexe"])
                if len(SexeL[SexeTmp])>3:
                    print(SexeL[SexeTmp])
                else:
                    print("Comment ça tu ne sais pas ce qu'est un (une) {} {}? Soit t'es un boulet, ou alors peut-être que cette description manque car {}.".format(Perso.RaceInfo["SexeType"], SexeTmp, ExcuseL[random.randint(0, len(ExcuseL) - 1)]))
                print("Veux tu choisir {} comme {}?".format(SexeTmp,Perso.RaceInfo["SexeType"]))
                if Input(["o","n"])=="o":
                    Perso.SexeType=Perso.RaceInfo["SexeType"]
                    Perso.Sexe=SexeTmp
                    SexeChoisi=True
    

    base=100
    Retirer="o"
    while Retirer!="n":
        c=Carac.InitializeCarac(base)
        delay_print("Les informations suivantes s'inscrivent sur l'écran: \n")
        for entry in list(c.keys()):
            delay_print("{:15}  :  {:>3}/100\n".format(entry,c[entry]))

        print("""

Pour information les valeurs indiqués sont les valeurs avant la prise en compte des modificateurs dûs à la race, l'age... \n
Veux tu retirer aléatoirement tes caractéristiques?
Attention la valeur maximale totale que tu pourra obtenir sera diminuée de 2.""")
        Retirer=Input(["o","n"])
        base-=2


    print("""Tu peux maintenant répartir 30 point comme tu le souhaite.
Si par exemple tu souhaites ajouter 10 points à la Précision entre :
Précision 10""")
    PointsLeft=30
    while PointsLeft!=0:
        try:
            rep=input().split()
            #            if rep[0] in c.keys():
            pp=min(PointsLeft,int(rep[1]))
            c[rep[0]]+=pp
            PointsLeft-=pp
            for entry in list(c.keys()):
                delay_print("{:15}  :  {:>3}/100\n".format(entry,c[entry]))

            print("""Il te reste {} points à répartir\n""".format(PointsLeft))
        except:
            print("Réponse non comprise\n Si par exemple tu souhaites ajouter 2 points à la Vitesse entre : \nVitesse 2\n")

    return c


def Malle(Perso):
    delay_print("Tu ouvres la malle, il n'y a rien dedans. Pas de chance. Ou alors c'est peut-être que les producteurs du jeu ont coupé les financements et que cela n'a pas permis au développeurs de finir ce jeu comme il faut et d'implémenter le choix d'un équipement... ou les développeurs sont peut être simplement des faignasses.\n")

        
def Mirroir(Perso):
    if Perso.Mirroir:
        delay_print("Tu te regardes dans le mirroir. Tu n'as pas changé depuis tout à l'heure")
        return
    delay_print("Tu te regardes dans le mirroir. C'est bon tu es bien toi-même.")

    print("""
Prend une feuille de papier. Découpe un rectangle de cette dimension : """)
    print("{28} ".format("_"))
    for i in range(13):
        print("|{27}|".format(""))
    print("|{27}| ".format("_"))
    Perso.Mirroir = True

    print("Sur le rectangle que tu viens de découper, dessine le portrait de ton personnage.")
