

def GetListMetiers():
    f=open("Métiers.tsv")
    lines=f.readlines()
    Metiers=dict()
    for line in lines[1:]:
        ls=line.split("\t")
        if len(ls[0])>1:
            Key0=ls[0]
            Metiers[Key0]=dict()
            Metiers[Key0]["Descr"]=ls[2]
            Metiers[Key0]["Comp"]=[ls[1]]
        else:
            Metiers[Key0]["Comp"].append(ls[1])
    return Metiers
