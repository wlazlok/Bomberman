import pygame as py, os

py.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = py.time.Clock()
fps = clock.tick(144)

volume = 1

font = py.font.Font('bm.ttf', 32)
font2 = py.font.Font('bm.ttf', 22)
screen = py.display.set_mode((1024, 768))

GROUND = 'ground.png'
WALL = 'slate.png'
BRICK = '2.png'
BOMB_UP = 'bomb.png'
POWER_UP = 'power.png'
LIFE_UP = 'life.png'
TIME_UP = 'clock.png'
PLAYER = 'player.png'

flaga = False
actual_level = 1
enemy_alive = actual_level + 2

backToMenu = py.image.load('images/do_menu.png').convert()
again = py.image.load('images/again.png').convert()
ground = py.image.load('images/tiles/ground.png').convert()


def clearBackground():
    bg = py.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    py.display.flip()
