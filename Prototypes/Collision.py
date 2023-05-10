import pyxel
from random import randint

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.pipesX = 0
        self.upperpipeY = 0
        self.height = 100
        self.width = 20
        self.playerX = 30
        self.playerY = 40
        self.vitesse = 2
        self.b = randint(20, 90) # upperpipe height
        self.lowerpipeY = self.b+40
        pyxel.run(self.update, self.draw)


    def update(self):
        self.pipesX = (self.pipesX - self.vitesse) % pyxel.width
        self.playerY = (self.playerY + 1) % pyxel.height
        self.collision()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.playerY = (self.playerY - 10)
        if self.pipesX == 0:
            self.b = randint(20, 90)
            self.lowerpipeY = self.b+40

    def collision(self):
        if self.playerY <= 0 or self.playerY >= 120:
            print("Out of border")
        else:
            if abs(self.playerX - self.pipesX) <= self.width:
                if self.playerY <= self.b + self.upperpipeY:
                    pyxel.quit()
                elif self.playerY + 15 >= self.lowerpipeY: #15 symbolise la hauteur du joueur
                    pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.pipesX, self.upperpipeY, self.width, self.b, 11) # Tuyau du haut
        pyxel.rect(self.pipesX, self.lowerpipeY, self.width, self.height, 11) # Tuyau du bas
        pyxel.rect(self.playerX, self.playerY, 15, 15, 8) # Joueur
App()
