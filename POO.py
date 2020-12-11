class Carte:

    def __init__ (self, valeur,couleur):
        self.valeur = valeur
        self.couleur = couleur
    def getAttributs(self):
        return(self.valeur,self.couleur)

    def getCouleur(self):
        return(self.couleur)
    def getValeur(self):
        return(self.valeur)

    def setCouleur(self,couleur):
        if couleur == "coeur" or couleur == "carreau" or couleur == "pique" or couleur =="trèfle":
            self.couleur = couleur
            return True
        else:
            return False

    def setValeur(self,v):
        if 2<=v <= 14:
            self.valeur= v
            return True
        else:
            return False