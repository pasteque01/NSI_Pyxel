import pyxel

from game import Game

class App:
    def __init__(self):
        pyxel.init(160, 120, "meow")
        pyxel.load("my_resource.pyxres") # génère les tuyaux et l'oiseau
        self.game = Game()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.game.update()

    def draw(self):
        pyxel.cls(0)
        self.game.draw()

App()
