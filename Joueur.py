#Class de création d'un joueur
"""Import jeuxcartes"""
import carte
nom = ""
# JeuxCarte = jeuxcarte(nbCarte=52)

carte = carte("Dame","Carreaux")

class mains:
    def __init__(self,carte):
        self.carte = carte



class Joueur:
    def __init__(self,nom,nbCartes,mainJoueur):
        self.nom = nom
        #self.nbCarte = JeuxCarte.getTailleDeJeu()


