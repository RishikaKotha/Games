import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')

# Board setup
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Fonts
font = pygame.font.SysFont(None, 60)

# Draw lines
def draw_lines():
    # Background
    screen.fill(WHITE)
    # Horizontal lines
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw X and O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, RED, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                                 CROSS_WIDTH)
                pygame.draw.line(screen, RED, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 CROSS_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, BLUE, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

# Check for a winner
def check_winner(player):
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row, player)
            return True

    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player)
            return True

    # Check main diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diagonal_win_line(player)
        return True

    # Check anti-diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        draw_anti_diagonal_win_line(player)
        return True

    return False

# Draw winning lines
def draw_horizontal_win_line(row, player):
    color = RED if player == 1 else BLUE
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.line(screen, color, (0, y), (WIDTH, y), LINE_WIDTH)

def draw_vertical_win_line(col, player):
    color = RED if player == 1 else BLUE
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.line(screen, color, (x, 0), (x, HEIGHT), LINE_WIDTH)

def draw_diagonal_win_line(player):
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (0, 0), (WIDTH, HEIGHT), LINE_WIDTH)

def draw_anti_diagonal_win_line(player):
    color = RED if player == 1 else BLUE
    pygame.draw.line(screen, color, (0, HEIGHT), (WIDTH, 0), LINE_WIDTH)

# Restart game
def restart():
    global board
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    draw_lines()

# Main loop
player = 1
game_over = False
draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # X-coordinate
            mouseY = event.pos[1]  # Y-coordinate

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = player
                if check_winner(player):
                    game_over = True
                player = 2 if player == 1 else 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()
