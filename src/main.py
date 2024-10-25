import pygame as pyg
# from sprite import Space_Shuttle

# CONSTANTS
FPS = 30
WIDTH = 640
HEIGHT = 480
WINDOW_TITLE = "Testing Apollo 13"
BACKGROUND_IMAGE = "assets/background_image.png"
SPACE_SHUTTLE = "assets/space_shuttle.png"

screen = pyg.display.set_mode((WIDTH, HEIGHT))

class Space_Shuttle(pyg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pyg.image.load("assets/space_shuttle.png")
        self.image.convert_alpha()
        self.image = pyg.transform.scale(self.image, (50, 50))

        # Make a rectangle
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.centery = 240
        
        # Creating the ability to move
        self.dx = 5

    def update(self):
        self.rect.centerx += self.dx

        # Checking the boundaries
        if self.rect.right > screen.get_width():
            self.rect.left = 0

def main() -> None:
    pyg.init()
    pyg.display.set_caption(WINDOW_TITLE)

    background = pyg.Surface(screen.get_size())
    background.fill("white")
    screen.blit(background, (0, 0))

    clock = pyg.time.Clock()

    running = True
    while running:
        clock.tick(FPS)
        space_shuttle = Space_Shuttle()
        test = pyg.sprite.Group(space_shuttle)

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False
        
        test.clear(screen, background)
        test.update()
        pyg.display.flip()

    pyg.quit()

if __name__ == "__main__":
    main()
