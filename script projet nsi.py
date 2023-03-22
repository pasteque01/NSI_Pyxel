import pyxel
from random import randint

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.pipetop = 0
        self.pipebot = 40
        self.score = 0 # Score constant durant la partie
        self.scorespeed = 0 # Score allant jusqu'à 5 pour l'accélérateur
        self.vitesse = 2
        self.b = randint(20, 90) # pos Y du tuyau du haut
        self.c = self.b+40 # Position y du tuyau du bas basée sur la pos Y du tuyau du haut
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)


    def update(self):
        self.pipetop = (self.pipetop - self.vitesse) % pyxel.width
        self.pipebot = (self.pipebot + 1) % pyxel.height
        if pyxel.btnp(pyxel.KEY_SPACE): # Saut
            self.pipebot = (self.pipebot - 10)
        if self.pipetop == 0: # Lorsqu'un tuyau passe à x=0:
            self.b = randint(20, 90)
            self.c = self.b+40
            self.score += 1
            self.scorespeed += 1
            print(self.scorespeed)
        if self.scorespeed == 5: # Tous les 5 tuyaux:
            self.scorespeed = 0
            self.vitesse += 0.5

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.pipetop, 0, 20, self.b, 11) # Tuyau du haut
        pyxel.rect(self.pipetop, self.c, 20, 100, 11) # Tuyau du bas
        pyxel.blt(20, self.pipebot, 0, 0, 0, 15, 15) # Joueur
        pyxel.text(5, 5, "Score:", 2)
        pyxel.text(30, 5, str(self.score), 2) # Dessine le score
App()