from frame import *
from button import *
import numpy as np

def playSample(self, instance, pos = None):
    instance.drum.play(self._padName)

class Pad(Button):
    def __init__(self, pos, size, instance, padName = "", parent = None):
        self._size = size
        self.parent = parent

        size = self.getSize()

        super().__init__(pos, size, parent, Texture("padOn.svg", size),Texture("padOff.svg", size))
        self._padName = padName
        self._instance = instance
        self.setPressCallback(playSample)

    def activate(self):
        self.press(self._instance)

    def deactivate(self):
        self.release(self._instance)

class PadZone(Frame):
    def __init__(self, instance, parent = None, pos = (0, 0), size = (0, 0)):
        super().__init__(pos, size, parent)

        margin = 0.0125

        sampleTab = [ "kick", "clap", "kick", "clap","kick", "clap", "kick", "clap"]

        numPad = sampleTab.__len__()
        numSpace = numPad - 1

        ratio = 0.85

        padW = (ratio / numPad)  * (1 - 2 * margin)
        spaceW = ((1 - ratio) / numSpace)  * (1 - 2 * margin)
        anchorX = margin
        anchorY = margin

        w, h = self.getSize()

        for sampleName in sampleTab:
            Pad((anchorX, anchorY), (padW, int(padW*w)), instance, sampleName, self)
            anchorX += padW + spaceW

    

    

