# -*- coding: utf-8 -*-


def SexeL():
    Sexes=dict()
    f = open("Galaxie Z - Sexes.tsv", 'r', encoding='utf8')
    lines=f.readlines()
    for line in lines[1:]:
        ls=line.split("\t")
        Sexes[ls[1]]=ls[2]

    return Sexes
