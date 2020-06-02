import config, pygame as py, board, titlescreen

class Final:
    def __init__(self, player):
        self.end = py.image.load('images/final.png').convert()
        config.flaga = False
        config.actual_level = 1
        board.clear()
        config.clearBackground()
        config.screen.blit(self.end, (0, 0))

        text = config.font.render("Your score: " + str(player.score), True, (255, 0, 1), (0, 0, 0))
        textrect = text.get_rect()
        textrect.center = (380, 200)
        config.screen.blit(text, textrect)

        py.display.flip()

        self.running = True

        while self.running:
            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_RETURN:
                        py.display.set_mode((1024, 768))
                        py.mixer.init()
                        py.mixer.music.load('sounds/title.wav')
                        py.mixer.music.play(-1)
                        py.mixer.music.set_volume(config.volume)
                        titlescreen.Titlescreen()
                        self.running = False
