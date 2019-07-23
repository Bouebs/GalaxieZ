

def Inventaire():
    f=open('Galaxie Z - Inventaire.tsv',encoding="utf-8")
    ListObj=[]
    for line in f.readlines()[46:]:
        ls=line.split("\t")
        try:
            Obj=dict([["ValMax",int(ls[1].split()[-1])],["Type",ls[2]],["Nom",ls[3]],["Matériau",ls[4]],["Description",ls[5]],["Poids",float(ls[6])]])
        except:
            print("ATTENTION PROBLEM DANS Inventaire.py")
            print(ls)
        if Obj["Nom"]!="Nef Ngometek" and Obj["Nom"]!="Perce-temps":
            ListObj.append(Obj)
            if len(ListObj)>1:
                if ListObj[-1]["ValMax"]<=ListObj[-2]["ValMax"]:
                    print("Il y a un problème dans la liste d'objet sur les valeurs pour le tirage aléatoire")

    return ListObj
