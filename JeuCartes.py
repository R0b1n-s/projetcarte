from valeursglobales import *
import random


class JeuCartes() :
    def _init_(self, nbCartes=52):
        self.nbCartes = nbCartes
        self.jeu = []
        self.creerJeu()


def getTailleJeu(self):
    return self.nbCartes

def creerJeu(self):
    for couleur in couleurs:
        for nom in noms:
            if (self.nbCartes == 32 and nom not in ['2','3','4','5','6']):
                self.jeu.append(Carte(nom, couleur))
            if (self.nbCartes == 52):
                self.jeu.append(Carte(nom, couleur))

def getJeu(self):
    return self.jeu

def melanger(self):
    return random.shuffle(self.jeu)

def distribuerCarte(self):
    derniereCarte= (self.jeu[-1])
    self.jeu.pop()
    return derniereCarte

def distribuerJeu(self, nbJoueurs, nbCartes):
    if (nbJoueurs*nbCartes<=self.nbCartes):
        tableau=[]
        for i in range(nbJoueurs):
            tableau.append([])
            for j in range(nbCartes):
                tableau[i].append(self.distribuerCarte())
        return tableau
    else:
        print("Pas assez de cartes dans le jeu")

def testJeuCartes():
    jeu52 = JeuCartes(52)
    jeu52.melanger

    L=jeu52.getJeu()
    carte = L[2]
    print('Nom:', carte.getNom())
    print('Couleur:', carte.getNom())
    print('Valeur:', carte.getNom())

    distribution_3j_4c = jeu52.distribuerJeu(3, 4)
    for i in range(3):
        print('Joueur', i+1, ':')
        listeCartes = distribution_3j_4c[i]
        for c in listeCartes:
            print(c.getNom(), 'de', c.getCouleur())




