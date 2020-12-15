from carte import *
from JeuCartes import*
from Joueur import *

class Bataille():
    def __init__(self, J1, J2, t_jeux,main1,main2):

        self.J1 = Joueur(J1,t_jeux,main1)
        self.J2 = Joueur(J2,t_jeux,main2) # valeur par défaut qui sera modifiée
        self.jeuCartes = JeuCartes(t_jeux) # valeur par défaut qui sera modifiée
        ## On mélange le jeu et on le distribue aux 2 joueurs

    def jouer(self):
        print("Debut:", self.jeuCartes)

        print(self.J1.getNom()," a gagné. Nombre de carte du joueur:",self.J1.getNbCartes())

def test():
    jeuxCarte = JeuCartes(52)
    print(jeuxCarte.getTailleJeu())
    main = jeuxCarte.creerJeu()
    a = jeuxCarte.distribuerJeu(2,jeuxCarte.getTailleJeu())
    d = jeuxCarte.distribuerJeu(2,jeuxCarte.getTailleJeu())
    jeuxCarte.melanger()
    j1 = Joueur("Rob",jeuxCarte.getTailleJeu(),a)
    j2 = Joueur("Pablo",jeuxCarte.getTailleJeu(),a)
    b = Bataille(j1,j2,jeuxCarte.getTailleJeu(),a,d)
    print(b.jouer())