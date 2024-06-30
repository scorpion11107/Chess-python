import core

core.pygame.init()

WINDOW_SIZE = (800, 800)
BUTTON_SIZE = (100, 100)
GRID_SIZE = 8

WHITE = (255, 255, 255)
GREEN = (30, 160, 30)
BLACK = (0, 0, 0)

screen = core.pygame.display.set_mode(WINDOW_SIZE)
core.pygame.display.set_caption('Grille de Boutons 8x8')

board = core.genBoard()
img_list = core.genImageList()

player_clicked = 0

def draw_board():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = core.pygame.Rect(col * BUTTON_SIZE[0], row * BUTTON_SIZE[1], BUTTON_SIZE[0], BUTTON_SIZE[1])
            if (col+row)%2 == 0:
                core.pygame.draw.rect(screen, WHITE, rect)
            else:
                core.pygame.draw.rect(screen, GREEN, rect)
            core.pygame.draw.rect(screen, BLACK, rect, 1)
            if img_list[board[row][col] + 6]:
            	screen.blit(img_list[board[row][col] + 6], rect.topleft)

running = True
while running:
    for event in core.pygame.event.get():
        if event.type == core.pygame.QUIT:
            running = False
        elif event.type == core.pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if not player_clicked:
                global pos1
                pos1 = (mouse_pos[1] // BUTTON_SIZE[1], mouse_pos[0] // BUTTON_SIZE[0])
                if board[pos1[0]][pos1[1]] != 0:
                    player_clicked = 1
            else:
                pos2 = (mouse_pos[1] // BUTTON_SIZE[1], mouse_pos[0] // BUTTON_SIZE[0])
                board = core.move_piece(pos1, pos2, board)
                player_clicked = 0
    
    screen.fill(WHITE)
    draw_board()
    core.pygame.display.flip()

core.pygame.quit()
