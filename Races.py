# -*- coding: utf-8 -*-
import io


def RacesL():
    Races=dict()

    Regne="Minéral"

    f = open("Galaxie Z - {}.tsv".format(Regne), 'r', encoding='utf8')

    lines=f.readlines()

    Races[Regne]=dict()
    
    Races["MinéralDescr"]=Races[Regne]["Description"]=lines[1].split("\t")[3]
    for line in lines[2:]:
        if len(line)<20:
            break
        ls=line.split("\t")
        RaceL=ls[2].split()[1]
        Races[Regne][RaceL]=dict()

        Races[Regne][RaceL]["Description"]=ls[3]
        Races[Regne][RaceL]["SexeType"]=ls[4]
        if ls[4]!="non":
            Races[Regne][RaceL]["Sexe"]=[]
            valsL=ls[5].split()
            for v in valsL:
                if v=="m":
                    Races[Regne][RaceL]["Sexe"].append("masculin")
                elif v=="f":
                    Races[Regne][RaceL]["Sexe"].append("feminin")
                else:
                    Races[Regne][RaceL]["Sexe"].append(v)
        Races[Regne][RaceL]["Intro"]=ls[6]
        Races[Regne][RaceL]["AgeMin"]=int(ls[7])
        Races[Regne][RaceL]["AgeMax"]=int(ls[8])
        Races[Regne][RaceL]["Bonus"]=dict()
        
        for Bonus in ls[9:]:
            if len(Bonus)>2:
                BS=Bonus.split()
                if "Max" in BS[1]:
                    Races[Regne][RaceL]["Bonus"][BS[0]]="Max 1"
                else:
                    Races[Regne][RaceL]["Bonus"][BS[0]]=int(BS[1])

        
        

# def Races():
#     Races=dict()
#     Races["Minéral"]=dict()
#     Races["Minéral"]["Lavinfern"]=dict([["Bonus",["Force",+1]],["Description","""La rxace Lavinfern est originaire d'une lune de Crematoria détruite lors du conflit Illyrien. Le corps des Lavinferns est constitué de lave et leur température naturelle avoisine les 1000 degrés Celsius. Entièrement fluides les Lavinferns sont lents comparativement à des humains mais ils peuvent déformer leur corps de façon à traverser différents milieux. Les Lavinferns sont très résistants mais ils sont très sensibles au froid ce qui les oblige à passer l'essentiel de leur temps social avec un scaphandre très isolant. Les Lavinfern ont dans la Galaxie plutôt mauvaise presse, de nombreux peuples ont des a prioris très négatifs pour cette race qui est souvent assimilé aux forces du mal. Dans leur longue histoire, les Lavinferns ont été à plusieurs reprises liés a des cabales mystiques du fait de leur très grande sensibilité aux fluctuations magiques."""]])
#     Races["Minéral"]["Crystallim"]=dict([["Bonus",["Endurance",+1]],["Description","""Les Crystallim sont des cristaux conscients. Leurs mouvements sont étonnament rapides étant donné leur mode de déplacement par croissance crystalline. Les Crystallims sont assez fragiles mais ont pour particularité de partager un esprit commun avec leurs congénères. Les spécialistes humains appellent cela la résonnance, les Crystallims semblent capables de vibrer sur une fréquence commune qui leur permet de se mettre en empathie. Dans cet état tous les crystallims présents dans la pièce agissent comme une seule entité consciente. Lors des guerres du Septant l'emporium scientifique Paragytt avait essayé d'inhiber cette capacité par des brouilleurs mais cela a été un échec qui leur a couté l'annihilation. Les Crystallim ont une durée de vie très courte, ce qui est souvent ignoré des autres races dans la mesure où ils croissent les uns à partir des autres. Il est très difficile de distinguer un individu d'un autre. Les Crystallims n'ont que très peu d'affinités avec les fluctuations magiques."""]])
#     Races["Minéral"]["Sab'eldune"]=dict([["Bonus",["Vitesse",+1]],["Description","""La race Sab'eldune est entièrement constitué d'une matière apparentée au sable. Les Sab'eldune prennent l'apparence d'une tempête de sable et sont en permanence en mouvement. Leur présence entraîne une perturbation électrique qui les a amené à développer des technologies essentiellement basées sur la mécanique. Les Sab'eldune peuvent prendre n'importe quelle forme et plusieurs témoignages affirment qu'ils peuvent se reconstituer à partir de n'importe quel matériaux sous forme de poussière (cendre, sable, farines, etc.) Les Sab'eldune sont généralement perçus comme un peuple vindicatif, leur rôle majeur à l'origine du conflit Illyrien est admis par la plupart des autres peuples. Pour beaucoup de peuples des autres races, les Sab'eldune sont tous les mêmes mais il existe en réalité une grande diversité de peuples parmi les Sab'eldune. Selon leurs historiens, les Sab'eldune seraient en réalité issus de deux races différentes originaires de système solaires différents. """]])
#     Races["Minéral"]["Cybornétikr"]=dict([["Bonus",["Perception",+1]],["Description","""La race Cybornétik est une des plus récentes races rattachée au règne minéral. Cette race autodéclarée réunit un groupe hétérogène de races issues de la robotique universelle. Après de longues années à développer des assistants robotisés, les diverses races de l'univers ont du statuer sur leur état d'être conscient. Après les procès de Nekat 20166 qui ont impliqués plusieurs miliers de systèmes solaires à travers l'univers, une large partie des robots ont acquis le statut de race à part entière. Leurs apparences sont variées et les technologies qui les animent également. En effet, les Cybornétik sont un agrégat d'être synthétiques conscients construits par les races naturelles à travers l'univers. La sensibilité des Cybornétik aux flux magiques est notoirement faible mais les publications scientifiques de Sociocybernétiques semblent montrer que la race est en train de se doter de nouvelles unités sensibles à la magie. Pour le moment elles sont encore très peu connues en dehors de leurs domaines."""]])
#     Races["Minéral"]["Ar'gyl"]=dict([["Bonus",["Précision",+1]],["Description","""Les Ar'gyl forment une société extrêmement fermée et hiérarchisée. Leurs relations avec les autres sociétés de l'univers se maintiennent au minimum vital. Leur planète de naissance semble entièrement composée d'Ar'gyl. En dehors des stations spatiales et de quelques vaisseaux d'exploration, la plupart des Ar'gyl restent sur leur planète natale. Les membres les plus récents ressemblent à des forment mouvantes d'argile tandis que les plus anciens s'enfoncent vers le coeur de la planète ce qui altère leur apparence et leur comportement. Les Ar'gyl les plus respectables sont ceux qui sont les plus proches du coeur de la planète. Le conflit Illyrien a amené les Ar'gyll a nuancer leur politique isolationniste, en s'ouvrant vers l'extérieur. En effet, la destruction de plusieurs planétoïdes leur a montré qu'ils étaient désormais directement menacés. Les Ar'gyl sont des pacifistes qui tentent d'influencer les autres peuples. Leur influence est désormais croissante à travers leur religion de type Gaïa qui affirme que tous les êtres conscients sont liés par la vie. Cette nouvelle croyance a amené certains des croyants, les Gaä'gyl à remettre en cause les conclusions des procès de Nekat en 20166. Pour les orthodoxes Gaä'gyl, les Cybornétik ne peuvent par revendiquer le statut de race dans la mesure où ils ne sont que des outils et non des êtres vivants."""]])
#     Races["Minéral"]["Grannti"]=dict([["Bonus",["Social",+2]],["Description","""Les Grannti sont une race d'être conscients dont la taille varie entre 5 et 7 mètres de haut. Ils sont d'une puissance physique et d'une résistance proverbiale en revanche leur intelligence moyenne est rarement supérieure à celle d'un enfant humain de 4 ou 5 ans. Leur formidable puissance physique a été très régulièrement mise à profit lors de conflits armés. Si bien que la culture des Grannti est désormais entièrement tournée autour des exploits militaires et des valeurs guerrières. Leur intelligence limitée les a obligé à rechercher des alliés pour mener leurs vies guerrières au delà des frontières de leurs mondes. Les Grannti sont très sociables et de bonne compagnie tout en se montrant impitoyables au combat et avec les traitres. Leur stature imposante et la légère radioactivité qu'ils génèrent en font tout de même des hôtes assez dangereux pour les races les plus fragiles. Ils ressemblent à des statues vivantes."""]])
#     Races["Minéral"]["Bazalti"]=dict([["Bonus",["Intelligence",+1]],["Description","""Le corps des membres de la race Bazalti est sombre et anguleux. Leur race est réputée pour son appétit pour les conflits et la brutalité de leurs moeurs. Leur intelligence est particulièrement raffinée, ils sont très rapides et font des combattants à la fois féroces et puissants. Jusqu'ici leur extension territoriale est limitée par leurs conflits internes. Les milliers de tribus de la race se partagent l'un des territoires les plus étendus de la Galaxie mais les frontières en sont très mouvantes et il n'est pas rare que les autres races profitent de leurs conflits internes pour coloniser l'une des planètes de leur territoire. Ce type d'agression extérieure peut parfois donner lieu à une alliance entre les tribus Bazalti, ce type d'alliance est appelée Sudourr. La Sudour commence par un combat rituel entre les champions des tribus qui font alliance, ce combat peut durer plusieurs dizaines d'années car les combattants Bazalti ne sont jamais touchés par la fatigue. L'histoire a montré qu'un Sudour n'est jamais une bonne nouvelle pour les autres races ce qui les a amené à comploter en permanence pour nourir les dissensions entre Bazalti."""]])
#     Races["Minéral"]["Corayy"]=dict([["Bonus",["Sensibilité",+1]],["Description","""La race Corayy est aquatique. Leur temporalité est tellement lente que lors des premiers contacts avec les humains, ces derniers ne prirent pas consience du fait qu'ils étaient conscients. Ils ont exploité le corps minéral d'une famille complète pendant soixante ans avant que ces derniers ne leur signalent très poliment qu'ils étaient en train de creuser des trous dans leur corps. Les humains durent payer des dommages et intérêts et présentèrent leurs excuses officiellement. Les Corayy ne revinrent jamais sur cette affaire et leurs relations diplomatiques sont excellentes avec les différents peuples de l'univers. La nature affable et pacifique des Corayy en fait de parfaits diplomates qui sont généralement sollicités pour régler les problèmes les plus épineux de la galaxie. Cependant, cela nécessite une logistique certaine puisque les Corayy vivent uniquement sous l'eau et à une pression équivalente à 30 fois celle de la surface terrestre. Pour cela, des ingénieurs humains ont créé des batiscaphes très modulaires qui permettent aux Corayy de se déplacer à travers la galaxie."""]])
#     Races["Minéral"]["Astreroidd"]=dict([["Bonus",["Volonté",+2]],["Description","""La race Astreroidd est l'une des plus mystérieuse actuellement connue. Les Astreroidd vivent dans l'espace, ils sont constitués de corps célestes qui ne semblent pas avoir le moindre moyen de se déplacer par eux même. Pourtant on les trouve toujours dans les lieux les plus habités de la galaxie. Leur habitat étant le vide, ils ont développé des moyens de communication basés uniquement sur les rayonnements électromagnétiques. C'est de cette manière qu'ils entrent en communication avec les autres peuples. Après une observation qui peut durer plusieurs années, les Astreroidd envoyent sur onde radio des messages aux vaisseaux des peuples intelligents qu'ils croisent. Il est impossible de distinguer un Astreroidd d'un autre corps céleste non conscient ce qui a pu créer au fil des siècles de nombreuses incompréhensions. Les Astreroidd semblent capables de vivre éternellement alors même qu'ils ne semblent pas avoir de nourriture, d'air ou même de moyen de se reproduire. Ils sont également très au courant de ce qui se passe pour les peuples des trois règnes. Certains peuples qui n'utilisent pas de technologie radio pour communiquer ont témoigné du fait que les Astreroidd semblaient pourtant connaître en détail leur culture et même les dernières actualités. Cela a poussé plusieurs théoriciens à imaginer que les Astreroidd avaient la possibilité de "hanter" d'autres être vivants en utilisant les flux magiques. Bien que cela n'ait jamais été prouvé, il est clair que les Astreroidd sont très souvent sollicités par les autres peuples lorsqu'il s'agit d'espionner ou d'obtenir des renseignements sur leurs ennemis. Leur nature en fait les espions parfaits."""]])

    return Races






