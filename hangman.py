import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the fonts
LETTER_FONT = pygame.font.SysFont(None, 40)
WORD_FONT = pygame.font.SysFont(None, 60)
TITLE_FONT = pygame.font.SysFont(None, 70)

# Load hangman images
images = []
for i in range(7):
    image = pygame.image.load(f"hangman{i}.png")
    images.append(image)

# Load words from a file
with open("words.txt", "r") as f:
    words = f.readlines()
words = [word.strip().upper() for word in words]

# Set up game variables
hangman_status = 0
word = random.choice(words)
guessed = []

# Set up button variables
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 400
A = 65

for i in range(26):
    x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = start_y + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Function to draw buttons
def draw_buttons():
    for letter in letters:
        x, y, char, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(char, 1, BLACK)
            win.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

# Function to draw the hangman image
def draw_hangman():
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

# Function to draw the word
def draw_word():
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

# Function to draw the game over message
def draw_game_over(status):
    if status == "win":
        message = "Congratulations! You won!"
        color = RED
    else:
        message = "Oops! You lost!"
        color = RED

    text = TITLE_FONT.render(message, 1, color)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

# Game loop
FPS = 60
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)
    win.fill(WHITE)
    draw_buttons()
    draw_hangman()
    draw_word()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame
