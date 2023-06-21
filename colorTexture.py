import pygame

class ColorTexture():
    def __init__(self, r, g, b, w, h):
        self.__surface = pygame.Surface((w, h))
        self.__surface.fill(pygame.Color(r, g, b))

    def getSurface(self):
        return self.__surface
