import io


def LoadFins():
    f = open("Galaxie Z - {}.tsv".format(Regne), 'r', encoding='utf8')
    f=open("Galaxie Z - Fins aléatoires 2078.tsv",encoding="utf-8")
    ListFins=[]
    for line in f.readlines()[1:]:
        fin=line.split("\t")[1]
        if len(fin)>3:
            ListFins.append(fin)

    return ListFins


def LoadPlanetes():
    f=open("Galaxie Z - Planètes.tsv",encoding="utf-8")
    ListPlanetes=dict()
    for regne in ["Minéral","Animal","Végétal"]:
        ListPlanetes[regne]=dict()
    for line in f.readlines()[1:]:
        if len(line)<4:
            continue
        print(line)
        ls=line.split("\t")
        if ls[4]=="o":
            ListPlanetes["Minéral"][ls[2]]=ls[3]
        if ls[5]=="o":
            ListPlanetes["Végétal"][ls[2]]=ls[3]
        if ls[6]=="o":
            ListPlanetes["Animal"][ls[2]]=ls[3]

    return ListPlanetes
