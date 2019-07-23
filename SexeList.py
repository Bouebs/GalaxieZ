# -*- coding: utf-8 -*-


def SexeL():
    Sexes=dict()
    f=open("Galaxie Z - Sexes.tsv")
    lines=f.readlines()
    for line in lines[1:]:
        ls=line.split("\t")
        Sexes[ls[1]]=ls[2]

    return Sexes
