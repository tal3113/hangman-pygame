from utils import WINDOW


# --------------- Constants  ---------------- #
HANGMAN_POS_X, HANGMAN_POS_Y = 50, 100


# ---------------- Classes  ----------------- #
class Hangman:
    def __init__(self, images):
        self.images = images
        self.hangman_status = 0

    def set_hangman_status(self):
        self.hangman_status += 1

    def get_hangman_status(self):
        return self.hangman_status

    def draw(self):
        WINDOW.blit(self.images[self.hangman_status], (HANGMAN_POS_X, HANGMAN_POS_Y))
