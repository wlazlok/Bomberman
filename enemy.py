import pygame as py, config, random, character, board, threading, time, bomb


class Enemy(character.Character):
    lives = 3
    currentBomb = 5
    power = 2

    def __init__(self, id, cos):

        self.cos = cos
        self.image = py.image.load('images/enemies/e_'+ str(id) +'_down.png').convert()
        self.image_up = py.image.load('images/enemies/e_'+ str(id) +'_up.png').convert()
        self.image_right = py.image.load('images/enemies/e_'+ str(id) +'_right.png').convert()
        self.image_left = py.image.load('images/enemies/e_'+ str(id) +'_left.png').convert()

        self.ground = py.image.load('images/tiles/ground.png').convert()
        self.bomb_image = py.image.load('images/bomb.png').convert()

        self.alive = True
        self.x, self.y = 0, 0

        self.thread1 = threading.Thread(target=self.randomize(), args=())
        self.thread1.start()

        config.screen.blit(self.image, (self.x, self.y))
        thread = threading.Thread(target=self.enemy_function, args=())
        thread.start()

    def getEXY(self):
        if self.alive:
            return (self.x, self.y)

    def enemy_function(self):
        if not self.alive:
            exit()
        while self.alive:
            self.move()
            if (self.x, self.y) in bomb.explode_range:
                self.cos.score += 100
                config.enemy_alive -= 1
                self.alive = False
                exit()
            if config.enemy_alive == 0:
                break
            if self.cos.lives == 0:
                break

    def randomize(self):
        self.x, self.y = int(random.randrange(120, 600, 40)), int(random.randrange(120, 600, 40))
        if (self.x, self.y) in board.walls or (self.x, self.y) in board.brick or (self.x, self.y) in board.enemies_alive or\
                ((self.x + 40, self.y) and (self.x - 40, self.y) and (self.x, self.y + 40) and (self.x, self.y - 40)) in board.walls or\
                ((self.x + 40, self.y) and (self.x - 40, self.y) and (self.x, self.y + 40) and (self.x, self.y - 40)) in board.brick:
            self.randomize()

    def move(self):
        time.sleep(0.5)
        side = int(random.randrange(273, 277))

        if side == 273:
            if self.y > 40:
                if (self.x, self.y - 40) not in board.walls and (self.x, self.y - 40) not in board.brick:

                    if list([self.x, self.y]) not in board.bomb_xy:
                        config.screen.blit(self.ground, (self.x, self.y))
                        self.y -= 40
                        config.screen.blit(self.image_up, (self.x, self.y))
                    else:
                        config.screen.blit(self.ground, (self.x, self.y))
                        config.screen.blit(self.bomb_image, (self.x, self.y))
                        self.y -= 40
                        config.screen.blit(self.image_up, (self.x, self.y))

        elif side == 274:
            if self.y < 600:
                if (self.x, self.y + 40) not in board.walls and (self.x, self.y + 40) not in board.brick:

                    if list([self.x, self.y]) not in board.bomb_xy:
                        config.screen.blit(self.ground, (self.x, self.y))
                        self.y += 40
                        config.screen.blit(self.image, (self.x, self.y))
                    else:
                        config.screen.blit(self.ground, (self.x, self.y))
                        config.screen.blit(self.bomb_image, (self.x, self.y))
                        self.y += 40
                        config.screen.blit(self.image, (self.x, self.y))

        elif side == 275:
            if self.x < 840:
                if (self.x + 40, self.y) not in board.walls and (self.x + 40, self.y) not in board.brick:

                    if list([self.x, self.y]) not in board.bomb_xy:
                        config.screen.blit(self.ground, (self.x, self.y))
                        self.x += 40
                        config.screen.blit(self.image_right, (self.x, self.y))
                    else:
                        config.screen.blit(self.ground, (self.x, self.y))
                        config.screen.blit(self.bomb_image, (self.x, self.y))
                        self.x += 40
                        config.screen.blit(self.image_right, (self.x, self.y))

        elif side == 276:
            if self.x > 40:
                if (self.x - 40, self.y) not in board.walls and (self.x - 40, self.y) not in board.brick:

                    if list([self.x, self.y]) not in board.bomb_xy:
                        config.screen.blit(self.ground, (self.x, self.y))
                        self.x -= 40
                        config.screen.blit(self.image_left, (self.x, self.y))
                    else:
                        config.screen.blit(self.ground, (self.x, self.y))
                        config.screen.blit(self.bomb_image, (self.x, self.y))
                        self.x -= 40
                        config.screen.blit(self.image_left, (self.x, self.y))

