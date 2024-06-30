import pygame

WHITE_PAWN = 1
WHITE_ROOK = 2
WHITE_KNIGHT = 3
WHITE_BISHOP = 4
WHITE_QUEEN = 5
WHITE_KING = 6

BLACK_PAWN = -6
BLACK_ROOK = -5
BLACK_KNIGHT = -4
BLACK_BISHOP = -3
BLACK_QUEEN = -2
BLACK_KING = -1


def genBoard():
    board = []
    
    board.append([-5, -4, -3, -2, -1, -3, -4, -5])
    board.append([-6 for i in range(8)])
    for i in range(4):
        board.append([0 for i in range(8)])
    board.append([1 for i in range(8)])
    board.append([2, 3, 4, 5, 6, 4, 3, 2])

    return board


def genImageList():
    res = []
    
    for i in range(2):
        for j in range(6):
            image = pygame.image.load(f'img\\{chr(66+i*21)}{j+1}.png')
            image = pygame.transform.scale(image, (100, 100))
            res.append(image)
        res.append(0)
    
    return res


def move_piece(pos1, pos2, board):
    piece = board[pos1[0]][pos1[1]]
    
    if pos1 == pos2:
        return board
    elif piece*board[pos2[0]][pos2[1]]>0:
        return board
    
    if (piece == 6 or piece == -1):
        if king_can_move(pos1, pos2):
            board[pos1[0]][pos1[1]] = 0
            board[pos2[0]][pos2[1]] = piece
            return board
        else:
            return board
    
    board[pos1[0]][pos1[1]] = 0
    board[pos2[0]][pos2[1]] = piece
    
    return board


def king_can_move(pos1, pos2):
    if abs(pos2[0]-pos1[0]) > 1 or abs(pos2[1]-pos1[1]) > 1:
        return False
    return True