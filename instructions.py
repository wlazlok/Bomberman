import config, pygame as py, titlescreen


class Instructions:
    def __init__(self):
        self.running = True

        imagePath = 'images/instructions.png'
        img = py.image.load(imagePath).convert()
        config.screen.blit(img, (0, 0))
        py.display.flip()

        while self.running:

            for events in py.event.get():
                if events.type == py.KEYDOWN:
                    if events.key == py.K_RETURN:
                        titlescreen.Titlescreen()
                        self.running = False

