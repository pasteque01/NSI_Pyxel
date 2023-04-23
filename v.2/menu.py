import pyxel

import game

class MainMenu:
    def __init__(self, game):
        self.game = game

    def update(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.game.new_game()

    def draw(self):
        pyxel.text(45, 12, "___________________", 1)
        pyxel.text(45, 23, "___________________", 1)
        pyxel.text(60, 20, "Flappy Bird", 10)
        pyxel.text(30, 40, "Press ENTER to START", 7)
        pyxel.text(30, 50, "Press ESC to QUIT", 7)
        pyxel.text(30, 60, "Latest Score:", 7)
        pyxel.text(90, 60, str(self.game.score), 9)
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.game.draw()