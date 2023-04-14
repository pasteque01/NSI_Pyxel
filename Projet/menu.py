import pyxel

import rawr #game file

class MainMenu:
    def __init__(self, game):
            self.game = game
            self.select_y = 50
            pyxel.stop()
            pyxel.playm(0, loop=True)

    def update(self, input):
        if pyxel.btn(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.rawr.__init__()

    def draw(self):
        pyxel.text(40, 20, "flappy bitch", 10)
