import pygame as py, config, board

bombPosition = [] # lista z pozycjami bomb


class Character:
    lives = 5
    score = 0
    currentBomb = 30
    power = 2

    def return_life(self):
        return self.lives

    def __init__(self):
        self.ground = py.image.load('images/tiles/ground.png').convert()
        self.image = 'images/players/down.png'
        self.bomb_image = py.image.load('images/bomb.png').convert()
        self.doors = py.image.load('images/tiles/doors_locked.png').convert()
        self.doors_mid = py.image.load('images/tiles/doors.png').convert()
        self.doors_open = py.image.load('images/tiles/doors_open.png').convert()
        self.image_start = py.image.load(self.image).convert()

        self.bomb = False
        self.x, self.y = 40, 40

        config.screen.blit(self.image_start, (40, 40))

    def start_pos(self):
        config.screen.blit(self.image_start, (40, 40))

    def getImage(self, direction):
        img = 'images/players/' + direction + ".png"
        self.image = py.image.load(img).convert()
        config.screen.blit(self.image, (self.x, self.y))

    def movement(self, key):

        if key == py.K_UP:
            self.getImage('up')
            self.move(key)  # 273

        elif key == py.K_DOWN:
            self.getImage('down')  # 274
            self.move(key)

        elif key == py.K_LEFT:
            self.getImage('left')  # 276
            self.move(key)

        elif key == py.K_RIGHT:
            self.getImage('right')  # 275
            self.move(key)

    def move(self, side):

        config.screen.blit(self.ground, (self.x, self.y))
        config.screen.blit(self.image, (self.x, self.y))

        if side == 273:
            if self.y > 40:

                if (self.x, self.y - 40) not in board.walls and (self.x, self.y - 40) not in board.brick:

                    if (self.x, self.y) in board.add_bomb:
                        self.currentBomb += 1
                        board.add_bomb.remove((self.x, self.y))

                    if (self.x, self.y) in board.life_pick:
                        self.lives += 1
                        board.life_pick.remove((self.x, self.y))

                    if (self.x, self.y) in board.bomb_powerup:
                        self.power += 1
                        board.bomb_powerup.remove((self.x, self.y))

                    if list([self.x, self.y]) not in board.bomb_xy:
                        config.screen.blit(self.ground, (self.x, self.y))
                        self.y -= 40
                        config.screen.blit(self.image, (self.x, self.y))
                        if (self.x, self.y + 40) in board.doors:
                            if config.enemy_alive == 0:
                                config.screen.blit(self.ground, (self.x, self.y + 40))
                                config.screen.blit(self.doors_open, (self.x, self.y + 40))
                            else:
                                config.screen.blit(self.ground, (self.x, self.y + 40))
                                config.screen.blit(self.doors, (self.x, self.y + 40))

                    else:
                        config.screen.blit(self.ground, (self.x, self.y))
                        config.screen.blit(self.bomb_image, (self.x, self.y))
                        self.y -= 40
                        config.screen.blit(self.image, (self.x, self.y))

        elif side == 274:
            if self.y < 600:

                if (self.x, self.y + 40) not in board.walls and (self.x, self.y + 40) not in board.brick:

                    if (self.x, self.y) in board.add_bomb:
                        self.currentBomb += 1
                        board.add_bomb.remove((self.x, self.y))

                    if (self.x, self.y) in board.life_pick:
                        self.lives += 1
                        board.life_pick.remove((self.x, self.y))

                    if (self.x, self.y) in board.bomb_powerup:
                        self.power += 1
                        board.bomb_powerup.remove((self.x, self.y))

                    if list([self.x, self.y]) not in board.bomb_xy:
                        config.screen.blit(self.ground, (self.x, self.y))
                        self.y += 40
                        config.screen.blit(self.image, (self.x, self.y))
                        if (self.x, self.y - 40) in board.doors:
                            if config.enemy_alive == 0:
                                config.screen.blit(self.ground, (self.x, self.y - 40))
                                config.screen.blit(self.doors_open, (self.x, self.y - 40))
                            else:
                                config.screen.blit(self.ground, (self.x, self.y - 40))
                                config.screen.blit(self.doors, (self.x, self.y - 40))

                    else:
                        config.screen.blit(self.ground, (self.x, self.y))
                        config.screen.blit(self.bomb_image, (self.x, self.y))
                        self.y += 40
                        config.screen.blit(self.image, (self.x, self.y))

        elif side == 275:
            if self.x < 840:

                if (self.x + 40, self.y) not in board.walls and (self.x + 40, self.y) not in board.brick:

                    if (self.x, self.y) in board.add_bomb:
                        self.currentBomb += 1
                        board.add_bomb.remove((self.x, self.y))

                    if (self.x, self.y) in board.life_pick:
                        self.lives += 1
                        board.life_pick.remove((self.x, self.y))

                    if (self.x, self.y) in board.bomb_powerup:
                        self.power += 1
                        board.bomb_powerup.remove((self.x, self.y))

                    if list([self.x, self.y]) not in board.bomb_xy:
                        config.screen.blit(self.ground, (self.x, self.y))
                        self.x += 40
                        config.screen.blit(self.image, (self.x, self.y))
                        if (self.x - 40, self.y) in board.doors:
                            if config.enemy_alive == 0:
                                config.screen.blit(self.ground, (self.x - 40, self.y))
                                config.screen.blit(self.doors_open, (self.x - 40, self.y))
                            else:
                                config.screen.blit(self.ground, (self.x - 40 , self.y))
                                config.screen.blit(self.doors, (self.x - 40, self.y))

                    else:
                        config.screen.blit(self.ground, (self.x, self.y))
                        config.screen.blit(self.bomb_image, (self.x, self.y))
                        self.x += 40
                        config.screen.blit(self.image, (self.x, self.y))

        elif side == 276:
            if self.x > 40:

                if (self.x - 40, self.y) not in board.walls and (self.x - 40, self.y) not in board.brick:

                    if (self.x, self.y) in board.add_bomb:
                        self.currentBomb += 1
                        board.add_bomb.remove((self.x, self.y))

                    if (self.x, self.y) in board.life_pick:
                        self.lives += 1
                        board.life_pick.remove((self.x, self.y))

                    if (self.x, self.y) in board.bomb_powerup:
                        self.power += 1
                        board.bomb_powerup.remove((self.x, self.y))

                    if list([self.x, self.y]) not in board.bomb_xy:
                        config.screen.blit(self.ground, (self.x, self.y))
                        self.x -= 40
                        config.screen.blit(self.image, (self.x, self.y))
                        if (self.x + 40, self.y) in board.doors:
                            if config.enemy_alive == 0:
                                config.screen.blit(self.ground, (self.x + 40, self.y))
                                config.screen.blit(self.doors_open, (self.x + 40, self.y))
                            else:
                                config.screen.blit(self.ground, (self.x + 40 , self.y))
                                config.screen.blit(self.doors, (self.x + 40, self.y))

                    else:
                        config.screen.blit(self.ground, (self.x, self.y))
                        config.screen.blit(self.bomb_image, (self.x, self.y))
                        self.x -= 40
                        config.screen.blit(self.image, (self.x, self.y))

    def getXY(self):
        return list([self.x, self.y])
