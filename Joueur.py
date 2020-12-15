from carte import *
from JeuCartes import *


class Joueur():
    def __init__(self, nom,nbCarte,mainJoueur):
        self.nom = nom
        self.nbCartes = nbCarte
        self.mainJoueur = mainJoueur


    def setMain(self,listeCartes):

        self.mainJoueur = listeCartes
        self.nbCartes= self.nbCartes + len(self.mainJoueur)

    def getNom(self):

        return self.nom

    def getNbCartes(self):

        return self.nbCartes

    def jouerCarte(self):

        derniereCarte= (self.mainJoueur[-1])

        if (derniereCarte == []):
            return "None"
        else:
            self.mainJoueur.pop()
            self.nbCartes = self.nbCartes - 1
            return derniereCarte

    def insererMain(self,CartesGagnees):

        for liste in CartesGagnees:
            self.mainJoueur.insert(0,liste)
            self.nbCartes = self.nbCartes +1
        return self.mainJoueur


def test():
    main = JeuCartes(52)
    main.creerJeu()
    a= main.getJeu()
    _joueur = Joueur("Rob",32,a)
    _joueur.setMain(a)
    print(_joueur.getNom())
    print(_joueur.getNbCartes())
    print(_joueur.jouerCarte())
