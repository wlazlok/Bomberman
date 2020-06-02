import board, character, pygame

class Play:
    def __init__(self, level):
        pygame.init()
        player = character.Character()
        b = board.Board(player)
        b.draw(1, player)


