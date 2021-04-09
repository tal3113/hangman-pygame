from utils import *
import os
import random
import requests
from display import Display


# --------------- Set Caption --------------- #
pygame.display.set_caption("Hangman")


# --------------- Constants  ---------------- #
FPS = 60


# -------------- Set Words site ------------- #
WORD_SITE = "https://www.mit.edu/~ecprice/wordlist.10000"


# --------------- Functions  ---------------- #
def set_words():
    response = requests.get(WORD_SITE)
    return response.content.splitlines()


def load_images():
    images = []
    for i in range(7):
        img = pygame.image.load(os.path.join("images", f"hangman{i}.png"))
        images.append(img)
    return images


def draw_message_screen(message, before_delay, after_delay):
    pygame.time.delay(before_delay)
    WINDOW.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    WINDOW.blit(text, ((WIDTH-text.get_width()) //
                       2, (HEIGHT-text.get_height())//2))
    pygame.display.update()
    pygame.time.delay(after_delay)


def game(words, images):
    word = random.choice(words).decode("utf-8").upper()
    # print(choose_word)
    display = Display(word, images)
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                display.mouse_click(pos_x, pos_y)

        display.draw_window()

        if display.is_won():
            draw_message_screen("You WON!",0,1000)
            break

        if display.is_lost():
            draw_message_screen(f"You Lost, The Word Was {word}",500,2000)
            break


def main():
    words = set_words()
    images = load_images()
    run_game = True
    while run_game:
        draw_message_screen("Press The Mouse To Begin",0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game(words, images)
    pygame.quit()


if __name__ == "__main__":
    main()
