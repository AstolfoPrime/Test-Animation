import pygame as pyg

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
        if self.rect.right > 640:
            self.rect.left = 0