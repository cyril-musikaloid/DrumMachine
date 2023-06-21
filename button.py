from frame import *
from pygameGraphic import *

class Button(Frame):
    def __init__(self, pos, size, parent = None, pressTexture = DummyTexture, releaseTexture = DummyTexture):
        super().__init__(pos, size, parent)

        size = self.getSize()
        if type(pressTexture) == str:
            self._pressTexture = Texture(pressTexture, size)
        else:
            self._pressTexture = pressTexture
        
        if type(releaseTexture) is str:
            self._releaseTexture = Texture(releaseTexture, size)
        else:
            self._releaseTexture = releaseTexture

        self._texture = self._releaseTexture
        self._pressed = False
        self._releaseCallback = None
        self._pressCallback = None

    def press(self, instance):
        if (self._pressCallback != None and not self._pressed):
            self._pressCallback(self,instance)

        
        self._texture = self._pressTexture
        self._pressed = True

    def release(self, instance, pos = (0, 0)):        
        if (self._releaseCallback != None and self._pressed):
            self._releaseCallback(self,instance, pos)

        self._texture = self._releaseTexture
        self._pressed = False

    def fingerDown(self,instance, pos = (0,0)):
        self.press(instance)

    def fingerUp(self, instance, pos = (0,0)):
        self.release(instance, pos)

    def setReleaseCallback(self, callback):
        self._releaseCallback = callback

    def setPressCallback(self, callback):
        self._pressCallback = callback
