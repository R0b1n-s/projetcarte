﻿#variables globales

couleurs = ('CARREAU','COEUR','TREFLE','PIQUE')
noms = ['2','3','5','6','7','8','9','10','Valet','Dame','Roi','As']
valeurs = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Valet':11,'Dame':12,'Roi':13,'As':14}
#classe carte
class Carte:
    def __init__(self, nom, couleur):
        #Affection des attributs nom et couleur avec contrôle.
        self.nom = nom
        self.couleur = couleur
        self.valeur = valeurs[nom]
############ Définition des méthodes d'instances avec contrôle #######
    def setNom(self, nom):
        if nom in noms:
            self.nom = nom
            self.valeur=valeurs[nom]
            return True
        else:
            return False

    def getNom(self):
        return self.nom
    def getCouleur(self):
        return self.couleur
    def getValeur(self):
        return self.valeur

    def egalite(self, carte):
        '''Renvoie True si les cartes ont la même valeur, False sinon carte: Objet de type Carte'''
        if carte.getValeur() == self.getValeur:
            return True
        else:
            return False


    def estSuperieureA(self, carte):
        ''' Renvoie True si la valeur de self est supérieure à celle de carte,
        False sinon
        carte: Objet de type Carte'''
        if carte.getValeur() > self.getValeur():
            return True
        else:
            return False

    def estInferieureA(self, carte):
        '''Renvoie True si la valeur e self est inférieure à celle de carte,
        False sinon
        carte: Objet de type Carte'''
        if carte.getValeur() < self.getValeur():
            return True
        else:
            return False



def TestCarte():#Test de la class Carte
    valetCoeur = Carte('Valet','Coeur')
    print("Nom:",valetCoeur.getNom())
    print('Couleur:',valetCoeur.getNom())
    print('Valeur:',valetCoeur.getValeur())
    valetCoeur.setNom('Dame')
    print('Nom modifié :',valetCoeur.getNom())
    print('Valeur modifié:',valetCoeur.getValeur())

    dameCoeur = Carte("Dame","CoooEur")
