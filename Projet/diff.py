import pyxel
from random import randint

class FlappyBird:
    def __init__(self):
        pyxel.init(160, 120, "meow")

        pyxel.load("my_resource.pyxres") # genere les tuyaux et l'oiseau
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):

        self.pipetop = 0 #position du tuyaux du haut
        self.pipebot = 40 #position du tuyaux du bas
        self.death = False #joueur pas mort
        self.score = 0 # Score constant durant la partie
        self.scorespeed = 0 # Score allant jusqu'à 5 pour l'accélérateur
        self.vitesse = 2 # vitesse des tuyaux au debut
        self.e = randint(-60, 20) #tuyaux aleatoire
        self.o = self.e +100 #tuyaux aleatoire


        pyxel.playm(0, loop=True)

    def update(self):

        if self.death == False: # si il est pas mort on charge toute les fonctions pour que le jeu soit fonctionnel
            self.update_player()
            self.update_pipes()
            self.update_score()
            self.check_death()

        if pyxel.btn(pyxel.KEY_Q): #quitter le jeu
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.reset()

    def update_player(self):
        if pyxel.btnp(pyxel.KEY_SPACE): # Saut
            self.pipebot = (self.pipebot - 10) # lorsque l'oiseau tombe et qu'on appuie sur espace il va remonter de 10 pixels

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
        if self.pipebot >= 108 or self.pipebot <= 0: # si l'oiseau sort du cadre = partie finie
            self.death_event()
        if self.pipebot >= 0 and self.pipebot <= self.e+71 and self.pipetop <= 32 and self.pipetop >= 20: # si il touche un tuyaux =partie finie
            self.death_event()


    def death_event(self):
        self.death = True


    def draw(self):
        if self.death == False:
            self.draw_pipes()
            self.draw_player()
            self.draw_score()
        else :
            self.draw_death()

    def draw_pipes(self):
        pyxel.cls(5)
        pyxel.blt(self.pipetop, self.e, 2, 0, 0, 32, 72)
        pyxel.blt(self.pipetop, self.o, 1, 0, 0, 32, 71)

    def draw_player(self) :
        pyxel.blt(20, self.pipebot, 0, 0, 0, 18, 12) # Joueur

    def draw_score(self):
        pyxel.text(5, 5, "Score:", 2)
        pyxel.text(30, 5, str(self.score), 2) # Dessine le score

    def draw_death(self):
        pyxel.cls(0)
        pyxel.text(60,45, "Game Over",8)
        pyxel.text(40,60, "Press R To Play Again",8)
        pyxel.text(42,75, "Press Q to quit game",8)



FlappyBird()
