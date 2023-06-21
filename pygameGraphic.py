import pygame
import frame

pygame.init()

class Window():
    def __init__(self,size=None):

        if size == None:
            self.__wnd = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        else:
            self.__wnd = pygame.display.set_mode(size=(1280, 720))

    def render(self, frame):
        frame.getTexture()._render(self.__wnd, frame.getPosition(True))
        frame.render(self)

    def update(self):
        pygame.display.flip()

    def getSize(self):
        return self.__wnd.get_size()

class ColorTexture():
    def __init__(self, r, g, b, size):
        self.__surface = pygame.Surface(size)
        self.__surface.fill(pygame.Color(r, g, b))

    def _getSurface(self):
        return self.__surface
    
    def _render(self, surface, pos):
        surface.blit(self.__surface, pos)

class Texture():
    def __init__(self, filename, size):
        self.__surface = pygame.image.load("./Textures/"+filename)
        s = self.__surface.get_size()
        self.__surface = pygame.transform.scale(self.__surface, size)

    def _getSurface(self):
        return self.__surface
    
    def _render(self, surface, pos):
        surface.blit(self.__surface, pos)

class Text():
    def __init__(self, text, size):
        font = pygame.font.SysFont("Arial", size=size)
        self.__surface = font.render(text, True, 0)

    def _getSurface(self):
        return self.__surface
    
    def _render(self, surface, pos):
        surface.blit(self.__surface, pos)

    def getSize(self):
        return self.__surface.get_size()