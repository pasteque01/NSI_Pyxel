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
        self.pipes = {}

    def new_game(self):
        self.main_menu = None
        self.game_over = None
        self.state = self.STATE_MAP #lors d'une nouvelle partie, l'etat du jeu est la map
        self.death = False #joueur pas mort
        self.score = 0 # Score constant durant la partie / a redéfinir lorsqu'on recommence la partie
        self.scorespeed = 0 # Score allant jusqu'à 5 pour l'accélérateur
        self.vitesse = 2 # vitesse des tuyaux au debut
        self.e = randint(-60, -10) #tuyau aleatoire
        self.o = self.e +110 #tuyau aleatoire
        self.pipetop = 100 #position du tuyau du haut
        self.player = 40
        self.pipes = {"Pipe1": [self.e, self.e+71, self.pipetop, self.pipetop+32], "Pipe2": [self.e, self.e+71, self.pipetop, self.pipetop+32]}

    def death_event(self): # retourne au menu
        self.state = self.STATE_GAMEOVER
        self.game_over = GameOver(self)

    def update(self):
        if self.state is self.STATE_MAP:
            self.update_player()
            self.update_pipes()
            self.update_score()
            self.check_death()
        elif self.state is self.STATE_MAIN_MENU: # si l etat = menu, on utilisera alors la fonction update de la class MainMenu
            self.main_menu.update()
        elif self.state is self.STATE_GAMEOVER:
            self.game_over.update()



    def update_player(self):
        if pyxel.btnp(pyxel.KEY_SPACE): # Saut
            self.player = (self.player - 10) # lorsque l'oiseau tombe et qu'on appuie sur espace il va remonter de 10 pixels

    def update_pipes(self):
        self.pipetop = (self.pipetop - self.vitesse) % pyxel.width
        self.player = (self.player + 1.5 ) % pyxel.height
        self.pipes = {"Pipe1": [self.e, self.e+71, self.pipetop], "Pipe2": [self.o, self.o+71, self.pipetop]} # Les valeurs "pipetop" restent les mêmes dans les 2 tuyaux pour l'instant; nous pouvons les changer pour faire varier la posX d'un tuyau sans affecter la collision

    def update_score(self):
        if self.pipetop == 0: # Lorsqu'un tuyau passe à x=0:
            self.e = randint(-60, -15)
            self.o = self.e +110
            self.score += 1
            self.scorespeed += 1
            print(self.pipes)
        if self.scorespeed == 5: # Tous les 5 tuyaux:
            self.scorespeed = 0
            self.vitesse += 0.5

    def check_death(self):
        if self.player >= 108 or self.player <= 0: # si l'oiseau sort du cadre = partie finie
            self.death_event()

        # Ancien code pour les collisions
        """if self.player >= self.e and self.player <= self.e+71 and self.pipetop <= 42 and self.pipetop >= 20:
            self.game_over()
        elif self.player >= self.o and self.pipetop <= 42 and self.pipetop >= 20:
            self.game_over()"""


        for x in self.pipes:
            if self.player >= self.pipes[x][0] and self.player <= self.pipes[x][1] and self.pipes[x][2] <= 48 and self.pipes[x][2] >= 30:
                self.death_event()


    """def update_gameover_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.state = self.STATE_MAP

        EXPLICATION:
        self.player = position Y de l'oiseau
        self.pipes = dictionnaire qui contient les coordonnées nécessaires pour les collisions
        > {"Tuyau": [posY du tuyau (en haut, à gauche), posY du tuyau (en bas, à gauche), posX du tuyau]}
        48 = position X de l'avant de l'oiseau
        30 = position X de l'arrière de l'oiseau

        SI l'oiseau se trouve entre le point Y en haut ET le point Y en bas ET la position X du tuyau se trouve entre l'avant ET l'arrière de l'oiseau
        > game_over()
        """


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
        pyxel.blt(self.pipetop, self.e, 2, 0, 0, 32, 72) #tuyau haut
        pyxel.blt(self.pipetop, self.o, 1, 0, 0, 32, 71) #tuyau bas

    def draw_player(self) :
        pyxel.blt(30, self.player, 0, 0, 0, 18, 12) # Joueur

    def draw_score(self):
        pyxel.text(5, 5, "Score:", 2)
        pyxel.text(30, 5, str(self.score), 2) # Dessine le score
