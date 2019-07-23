from Competences import *
import Metier
Metiers=Metier.GetListMetiers()
print
CompList=ReadCompList()
for MetierL in Metiers.keys():
    for Comp in Metiers[MetierL]["Comp"]:
        if not FindCompInCompList(Comp,CompList):
            print("La compétence {} du Métier {} n'a pas été trouvée".format(Comp,MetierL))
