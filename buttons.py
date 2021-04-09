from utils import WINDOW, BLACK, RADIUS, WIDTH, LETTER_FONT, pygame


# --------------- Constants  ---------------- #
NUM_OF_LETTERS = 26

# button variables
GAP = 15
START_X = round((WIDTH - (RADIUS*2+GAP)*13)/2)
START_Y = 400


# ---------------- Classes  ----------------- #
class LetterButton:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter
        self.visible = True

    def is_inside_button(self):
        self.visible = False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_letter(self):
        return self.letter

    def get_visible(self):
        return self.visible


class LetterButtons:
    def __init__(self):
        self.letters = []
        self.set_letters()
        self.guessed = []

    def set_letters(self):
        letter = 65  # A = 65
        for i in range(NUM_OF_LETTERS):
            x = START_X + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
            y = START_Y + ((i // 13) * (GAP + RADIUS * 2))
            letter_button = LetterButton(x, y, chr(letter + i))
            self.letters.append(letter_button)

    def get_letters(self):
        return self.letters

    def get_guessed(self):
        return self.guessed

    def add_to_guessed(self, ltr):
        self.guessed.append(ltr)

    def if_inside_button(self, letter):
        letter.is_inside_button()
        self.add_to_guessed(letter.get_letter())

    def draw(self):
        for letter in self.letters:
            if letter.visible:
                pygame.draw.circle(
                    WINDOW, BLACK, (letter.get_x(), letter.get_y()), RADIUS, 3)
                letter_text = LETTER_FONT.render(letter.get_letter(), 1, BLACK)
                WINDOW.blit(letter_text, (letter.get_x() - letter_text.get_width() /
                                          2, letter.get_y() - letter_text.get_height()/2))
