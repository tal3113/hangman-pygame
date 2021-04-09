import math
from utils import WHITE, RADIUS, WINDOW, pygame
from hangman import Hangman
from word import Word
from buttons import LetterButtons


# ---------------- Classes  ----------------- #
class Display:
    def __init__(self, word, images):
        self.hangman = Hangman(images)
        self.word = Word(word)
        self.letter_buttons = LetterButtons()

    def is_letter_not_in_word(self, ltr):
        if ltr not in self.word.get_word():
            self.hangman.set_hangman_status()

    def mouse_click(self, mouse_x, mouse_y):
        letters = self.letter_buttons.get_letters()
        for letter in letters:
            if letter.get_visible():
                distance = math.sqrt((letter.get_x() - mouse_x)
                                     ** 2 + (letter.get_y() - mouse_y)**2)
                if distance < RADIUS:
                    self.letter_buttons.if_inside_button(letter)
                    self.is_letter_not_in_word(letter.get_letter())

    def draw_window(self):
        WINDOW.fill(WHITE)
        self.word.draw(self.letter_buttons.get_guessed())
        self.letter_buttons.draw()
        self.hangman.draw()
        pygame.display.update()

    def is_won(self):
        for letter in self.word.get_word():
            if letter not in self.letter_buttons.get_guessed():
                return False
        return True

    def is_lost(self):
        return self.hangman.get_hangman_status() == 6
