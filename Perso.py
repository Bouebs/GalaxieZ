from Carac import *


class Personnage:
    def __init__(self):
        Nom = None
        Age = None
        Sexe = None
        SexeType = None
        Planete = None
        Race = None
        Regne= None
        Descr= None
        self.print_speed = 0
        CaracBase = InitializeCarac(None)
        self.Carac = InitializeCarac(None)
        Comp = None
        self.Miroir = False
