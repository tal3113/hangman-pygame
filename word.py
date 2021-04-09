from utils import BLACK, WIDTH, WINDOW, WORD_FONT

# --------------- Constants  ---------------- #
IMG_WIDTH, IMG_HEIGHT = 209, 216


# ---------------- Classes  ----------------- #
class Word():
    def __init__(self, word):
        self.word = word

    def set_display_word(self, guessed):
        display_word = ""
        for letter in self.word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        return display_word

    def draw(self, guessed):
        display_word = self.set_display_word(guessed)
        word_text = WORD_FONT.render(display_word, 1, BLACK)
        center_x = IMG_WIDTH + (WIDTH - IMG_WIDTH)//2
        WINDOW.blit(word_text, ((center_x - word_text.get_width()) //
                                2 + IMG_WIDTH, IMG_HEIGHT))

    def get_word(self):
        return self.word
