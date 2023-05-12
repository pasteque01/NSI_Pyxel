import pyxel

from random import randint

from menu import MainMenu # importe la class MainMenu du script menu.py

from game_over import GameOver

class Game:
    # ETAT DU JEU
    # 0 = le jeu est dans le menu, 1 = le jeu est dans la map
    STATE_MAIN_MENU = 0
    STATE_MAP = 1
    STATE_GAMEOVER = 2

    def __init__(self):
        # Dès l'execution du jeu, l'etat du jeu est dans le menu
        self.state = self.STATE_MAIN_MENU
        self.main_menu = MainMenu(self) #fait reference a la class MainMenu dans menu.py
        self.game_over = GameOver(self)
        self.score = 0 #score par defaut
        self.highscore = 0

        self.upperpipeY = 0
        self.height = 100
        self.width = 23


    def new_game(self):
        self.main_menu = None
        self.game_over = None
        self.state = self.STATE_MAP #lors d'une nouvelle partie, l'etat du jeu est la map
        self.death = False #joueur pas mort
        self.score = 0 # Score constant durant la partie / a redéfinir lorsqu'on recommence la partie
        self.scorespeed = 0 # Score allant jusqu'à 5 pour l'accélérateur
        self.vitesse = 2 # vitesse des tuyaux au debut


        self.b = randint(-60, -10) #tuyau aleatoire
        self.height = self.b +110 #tuyau aleatoire
        self.pipesX = 100 #position du tuyau du haut
        self.c = randint(-60, -10) #tuyau aleatoire
        self.height1 = self.c +110 #tuyau aleatoire
        self.pipesX1 = 150 #position du tuyau du haut
        self.dico = {}


        self.playerY = 40
        self.playerX = 40

    def death_event(self): # retourne au menu
        self.state = self.STATE_GAMEOVER
        self.game_over = GameOver(self)

    def update(self):
        if self.state is self.STATE_MAP:
            self.update_player()
            self.update_pipes()
            self.update_score()
            self.collision()
        elif self.state is self.STATE_MAIN_MENU: # si l etat = menu, on utilisera alors la fonction update de la class MainMenu
            self.main_menu.update()
        elif self.state is self.STATE_GAMEOVER:
            self.game_over.update()



    def update_player(self):
        if pyxel.btnp(pyxel.KEY_SPACE): # Saut
            self.playerY = (self.playerY - 10) # lorsque l'oiseau tombe et qu'on appuie sur espace il va remonter de 10 pixels

    def update_pipes(self):
        self.pipesX = (self.pipesX - self.vitesse) % pyxel.width
        self.pipesX1 = (self.pipesX1 - self.vitesse) % pyxel.width
        self.playerY = (self.playerY + 1.5 ) % pyxel.height
        self.dico = {"pipehaut" : [self.pipesX,self.b,2], "pipebas" : [self.pipesX,self.height,1], "pipehaut1" : [self.pipesX1,self.c,2], "pipebas1" : [self.pipesX1,self.height1,1]}

    def update_score(self):
        if self.pipesX == 0: # Lorsqu'un tuyau passe à x=0:
            self.b = randint(-60, -15)
            self.height = self.b +110
            self.c = randint(-60, -10) #tuyau aleatoire
            self.height1 = self.c +110 #tuyau aleatoire
            self.score += 1
            self.scorespeed += 1
        if self.scorespeed == 5: # Tous les 5 tuyaux:
            self.scorespeed = 0
            self.vitesse += 0.5

    def collision(self):
        if self.playerY <= 0 or self.playerY >= 120:
            self.death_event()
        else:
            for x in self.dico:
                if abs(self.playerX - self.pipesX) <= self.width:
                    if self.playerY <= self.b + 70:
                        self.death_event()
                    elif self.playerY + 13 >= self.height: #15 symbolise la hauteur du joueur
                        self.death_event()


    def draw(self):
        if self.state is self.STATE_MAP:
            self.draw_pipes()
            self.draw_player()
            self.draw_score()
        elif self.state is self.STATE_MAIN_MENU:
            self.main_menu.draw()
        elif self.state is self.STATE_GAMEOVER:
            self.game_over.draw()


    def draw_pipes(self):
        pyxel.cls(5)
        #pyxel.blt(self.pipesX, self.b, 2, 0, 0, self.width, 72) #tuyau haut
        #pyxel.blt(self.pipesX, self.height, 1, 0, 0, self.width, 72) #tuyau bas
        for y in self.dico:
            pyxel.blt(self.dico[y][0],self.dico[y][1],self.dico[y][2],0, 0, self.width, 72)



    def draw_player(self) :
        pyxel.blt(self.playerX, self.playerY, 0, 0, 0, 18, 12) # Joueur

    def draw_score(self):
        pyxel.text(5, 5, "Score:", 2)
        pyxel.text(30, 5, str(self.score), 2) # Dessine le score
