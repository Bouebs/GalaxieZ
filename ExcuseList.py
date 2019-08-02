# -*- coding: utf-8 -*-

def ExcuseL():
    Ex=[]
    f = open("Galaxie Z - Excuses.tsv", 'r', encoding='utf8')
    lines=f.readlines()
    f.close()
    for line in lines[1:]:
        Ex.append(line)

    return Ex
