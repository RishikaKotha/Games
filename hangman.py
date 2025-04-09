import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
MESSAGE_FONT = pygame.font.SysFont("comicsans", 50)

# Hangman images
hangman_images = []
for i in range(7):
    image = pygame.image.load(f"hangman{i}.png")
    hangman_images.append(image)

# Game variables
words = ["PYTHON", "HANGMAN", "PYGAME", "DEVELOPER", "PROGRAMMING"]
word = random.choice(words)
guessed = []
hangman_status = 0

# Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65  # ASCII value for 'A'

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])


# Functions
def draw():
    screen.fill(WHITE)

    # Draw title
    text = WORD_FONT.render("HANGMAN", True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, True, BLACK)
    screen.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, char, visible = letter
        if visible:
            pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(char, True, BLACK)
            screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    # Draw hangman
    screen.blit(hangman_images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    screen.fill(WHITE)
    text = MESSAGE_FONT.render(message, True, RED)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


# Main game loop
run = True
while run:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, char, visible = letter
                if visible:
                    distance = ((x - m_x) ** 2 + (y - m_y) ** 2) ** 0.5
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(char)
                        if char not in word:
                            hangman_status += 1

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("You Won!")
        break

    if hangman_status == 6:
        display_message("You Lost!")
        break

pygame.quit()
sys.exit()
