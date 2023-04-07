import pyxel
from random import randint

class FlappyBird:

    def __init__(self):
        pyxel.init(160, 120)
        self.pipetop = 0
        self.pipebot = 40
        self.death = False
        self.score = 0 # Score constant durant la partie
        self.scorespeed = 0 # Score allant jusqu'à 5 pour l'accélérateur
        self.vitesse = 2
        self.e = randint(-60, 20)
        self.o = self.e +100
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)


    def update(self):

        if not self.death :
            self.update_player()
            self.update_pipes()
            self.update_score()
            self.death_event()
            self.check_death()

    def update_player(self):
        if pyxel.btnp(pyxel.KEY_SPACE): # Saut
            self.pipebot = (self.pipebot - 10)

    def update_pipes(self):
        self.pipetop = (self.pipetop - self.vitesse) % pyxel.width
        self.pipebot = (self.pipebot + 1.5 ) % pyxel.height

    def update_score(self):
        if self.pipetop == 0: # Lorsqu'un tuyau passe à x=0:
            self.e = randint(-60, 20)
            self.o = self.e +100
            self.score += 1
            self.scorespeed += 1
            print(self.scorespeed)
        if self.scorespeed == 5: # Tous les 5 tuyaux:
            self.scorespeed = 0
            self.vitesse += 0.5

    def check_death(self):
        if self.pipebot >= 108 :
            self.death_event()


    def death_event(self):
        self.death = True
        pyxel.stop()
        pyxel.play(0, 1)


    def draw(self):

        if not self.death :
            pyxel.cls(5)
            pyxel.blt(self.pipetop, self.e, 2, 0, 0, 32, 71)
            pyxel.blt(self.pipetop, self.o, 1, 0, 0, 32, 71)
            pyxel.blt(20, self.pipebot, 0, 0, 0, 18, 12) # Joueur
            pyxel.text(5, 5, "Score:", 2)
            pyxel.text(30, 5, str(self.score), 2) # Dessine le score

        else :
            pyxel.cls(0)


FlappyBird()


