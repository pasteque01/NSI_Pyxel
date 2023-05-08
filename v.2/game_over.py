import pyxel

import game

class GameOver:
    def __init__(self, game):
        self.game = game

    def update(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.game.new_game()
        if self.game.highscore < self.game.score:
            self.game.highscore = self.game.score

    def draw(self):
        pyxel.text(60, 30, "GAME OVER", 8)
        pyxel.text(30, 50, "SCORE:", 7)
        pyxel.text(100, 50, str(self.game.score), 9)
        pyxel.text(30, 80, "Press ENTER to RESTART", 7)
        pyxel.text(30, 95, "Press ESC to QUIT", 7)
        pyxel.text(30, 65, "HIGHEST Score:", 7)
        pyxel.text(100, 65, str(self.game.highscore), 9)