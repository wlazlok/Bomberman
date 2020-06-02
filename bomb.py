import pygame as py, config
import time
import threading
import board, character

explode_range = []  # lista z zasiegiem wybuchu bomb


class Bomb(threading.Thread):

    def __init__(self, x, y, power, doors, player):
        threading.Thread.__init__(self)
        py.mixer.init()
        self.doors = doors
        self.start()
        self.x = x
        self.y = y
        self.power = power + 1
        self.bomb_image = py.image.load('images/bomb.png').convert()
        self.ground = py.image.load('images/tiles/ground.png').convert()
        self.explosion = py.image.load('images/explosion_a.png').convert()
        self.explosion_v = py.image.load('images/vertical.png').convert()
        self.explosion_h = py.image.load('images/horizontal.png').convert()
        self.bomb_powerup = py.image.load('images/tiles/power.png').convert()
        self.life_pick = py.image.load('images/tiles/life.png').convert()
        self.add_bomb = py.image.load('images/tiles/bomb.png').convert()
        self.doors = py.image.load('images/tiles/doors.png').convert()
        self.doors_locked = py.image.load('images/tiles/doors_locked.png').convert()
        self.doors_open = py.image.load('images/tiles/doors_open.png').convert()

        self.draw_bomb()
        self.player = player

    def draw_bomb(self):
        config.screen.blit(self.bomb_image, (self.x, self.y))

    def explode(self):
        config.screen.blit(self.ground, (self.x, self.y))
        config.screen.blit(self.explosion, (self.x, self.y))
        py.mixer.Channel(0).set_volume(0.6)
        py.mixer.Channel(0).play(py.mixer.Sound('sounds/blast_01.wav'))
        bricks = []
        destroy = [list([self.x, self.y])]

        explode_range.append((self.x, self.y))

        for i in range(self.power):
            if i == 0:
                continue
            if (self.x, self.y - (40 * i)) in board.walls:
                break
            if (self.x, self.y - (40 * i)) not in board.walls:
                config.screen.blit(self.explosion_v, (self.x, self.y - (40 * i)))
                destroy.append((self.x, self.y - (40 * i)))
                explode_range.append((self.x, self.y - (40 * i)))
                if (self.x, self.y - (40 * i)) in board.brick:
                    bricks.append(list([self.x, self.y - (40 * i)]))

        for i in range(self.power):
            if i == 0:
                continue
            if (self.x, self.y + (40 * i)) in board.walls:
                break
            if (self.x, self.y + (40 * i)) not in board.walls:
                config.screen.blit(self.explosion_v, (self.x, self.y + (40 * i)))
                destroy.append((self.x, self.y + (40 * i)))
                explode_range.append((self.x, self.y + (40 * i)))
                if (self.x, self.y + (40 * i)) in board.brick:
                    bricks.append(list([self.x, self.y + (40 * i)]))

        for i in range(self.power):
            if i == 0:
                continue
            if (self.x - (40 * i), self.y) in board.walls:
                break
            if (self.x - (40 * i), self.y) not in board.walls:
                config.screen.blit(self.explosion_h, (self.x - (40 * i), self.y))
                destroy.append((self.x - (40 * i), self.y))
                explode_range.append((self.x - (40 * i), self.y))

                if (self.x - (40 * i), self.y) in board.brick:
                    bricks.append(list([self.x - (40 * i), self.y]))

        for i in range(self.power):
            if i == 0:
                continue
            if (self.x + (40 * i), self.y) in board.walls:
                break
            if (self.x + (40 * i), self.y) not in board.walls:
                config.screen.blit(self.explosion_h, (self.x + (40 * i), self.y))
                destroy.append((self.x + (40 * i), self.y))
                explode_range.append((self.x + (40 * i), self.y))

                if (self.x + (40 * i), self.y) in board.brick:
                    bricks.append(list([self.x + (40 * i), self.y]))

        time.sleep(1)

        if self.player.lives <= 0:
            destroy.clear()
        for i in range(len(destroy)):
            config.screen.blit(self.ground, (destroy[i]))
            for x in range(len(board.bomb_powerup)):
                if destroy[i] in board.bomb_powerup:
                    config.screen.blit(self.bomb_powerup, (destroy[i]))

            for x in range(len(board.life_pick)):
                if destroy[i] in board.life_pick:
                    config.screen.blit(self.life_pick, (destroy[i]))

            for x in range(len(board.add_bomb)):
                if destroy[i] in board.add_bomb:
                    config.screen.blit(self.add_bomb, (destroy[i]))

            for x in range(len(board.doors)):
                if destroy[i] in board.doors and self.doors:
                    board.draw_doors()

            if destroy[i] in board.brick:
                board.brick.remove(destroy[i])
            explode_range.clear()
        exit()

    def pos_return(self):
        pos = (self.x, self.y)
        return pos

    def run(self):
        time.sleep(3)
        thread = threading.Thread(target=self.explode, args=())
        thread.start()
        board.bomb_xy.pop(-1)
