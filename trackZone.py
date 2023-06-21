from frame import *
from button import *

def doPlay(self:Button, instance):
    instance.isPlaying = True

def doPause(self:Button, instance):
    instance.isPlaying = False


class TrackToolBar(Frame):
    def __init__(self, parent = None, pos = (0, 0), size = (0, 0)):
        super().__init__(pos, size, parent)

        size = self.getSize()
        sizeW, sizeH = size
        buttonSize = (sizeH, sizeH)
        play = Button((0, 0), buttonSize, self,
                      "playPress.svg", "playRelease.svg")
        play.setPressCallback(doPlay)

        pause = Button((sizeH, 0), buttonSize, self,
                       "pausePress.svg", "pauseRelease.svg")
        pause.setPressCallback(doPause)

class TrackName(Frame):
    def __init__(self, name = "", parent = None, pos = (0, 0), size = (0, 0)):
        self.setTexture(Text(name, size[1]))

        textSize = self.getTexture().getSize()
        trackNameBg = Frame(size=textSize, parent=parent, pos=pos)
        trackNameBg.setTexture(Texture("trackNameBg.svg", textSize))
        super().__init__((0, 0), size, trackNameBg)

class TrackTool(Frame):
    def __init__(self, name = "", parent = None, pos = (0, 0), size = (0, 0)):
        super().__init__(pos, size, parent)

        size = self.getSize()
        self.setTexture(Texture("trackToolBg.svg", size))

        w, h = size

        h2 = int(h /1.8)

        x = 0
        y = int(h / 2 - h2 / 2)
        trackName = TrackName(name, pos=(x, y), size=(w, h2), parent=self)
                    

class Track(Frame):
    def __init__(self, trackData, parent = None, pos = (0, 0), size = (0, 0)):
        super().__init__(pos, size, parent)

        self._data = trackData

class TrackPart(Frame):
    def __init__(self, trackName, instance, parent = None, pos = (0, 0), size = (0,0), lineTexture=DummyTexture):
        super().__init__(pos, size, parent)

        Frame(size=(-1, 1), parent=self).setTexture(lineTexture)
        Frame((0, -1), size=(-1, 1), parent=self).setTexture(lineTexture)

        self.trackName = trackName
        self.trackData = instance.tracks[trackName]
        self.instance = instance


    def fingerDown(self, instance, pos=(0, 0)):
        hitX, hitY = self.globalToLocal(pos)

        stepHit = self.xToStep(hitX)

        if stepHit in self.trackData:
            self.trackData.remove(stepHit)

        else:
            self.trackData.add(stepHit)

    def render(self, window):
        super().render(window)

        instance = self.instance

        w, h = self.getSize()

        numStep = int(instance.numberDisplayedStep + 1)
        stepWidth = w / instance.numberDisplayedStep
        timestamp = instance.timestamp
        stepDuration = instance.getStepDurationMS()
        offset = int(stepWidth * timestamp / stepDuration)

        self.parent.activatedTexture = ColorTexture(200, 58, 58, (stepWidth, h))
        for i in range(0, numStep):
            step = int((i * stepWidth + offset) / stepWidth)

            if (step in self.trackData and int(step * stepWidth) - offset >= 0):
                framePos = (
                    int(step * stepWidth) - offset,
                    0
                )
                window.render(Frame(framePos, (int(stepWidth), h), self, False, self.parent.activatedTexture))

    def getStepWidth(self):
        return self.parent.getStepWidth()

    def getXOffset(self):
         return self.parent.getXOffset()
    
    def xToStep(self, x:int):
        return self.parent.xToStep(x)

class PartZone(Frame):
    def __init__(self, instance, parent = None, pos = (0, 0), size = (0, 0)):
        super().__init__(pos, size, parent)
        
        w, h = self.getSize()
        self.instance = instance
        self.horizontalLineTexture = ColorTexture(175, 175, 175, (w, 1))
        self.verticalLineTexture = ColorTexture(175, 175, 175, (1, h))
        self.activatedTexture = ColorTexture(200,58, 58, (1,1))
        self.verticalLines = []

    def render(self, window):
        self.verticalLines.clear()

        w, h = self.getSize()

        instance = self.instance
        timestamp = instance.timestamp
        stepDuration = instance.getStepDurationMS()
        numberStep = instance.numberDisplayedStep
        stepWidth = w / numberStep

        offset = (timestamp % stepDuration) / stepDuration


        for i in range(0, int(numberStep + 1)):
            window.render(Frame((int(((i * (1 / numberStep)) * w) - (stepWidth * offset)), 0),
                                (1, -1), self, False,
                                self.verticalLineTexture))


        super().render(window)
        
    def getStepWidth(self):
        w, h = self.getSize()
        return w / self.instance.numberDisplayedStep

    def getXOffset(self):
         return int(self.getStepWidth() * self.instance.timestamp / self.instance.getStepDurationMS())

    def xToStep(self, x:int):
        return int((self.getXOffset() + x) / self.getStepWidth())

class TrackZone(Frame):
    def __init__(self, instance, parent = None, pos = (0, 0), size = (0, 0)):
        super().__init__(pos, size, parent)

        self.instance = instance
        

        separator = 0.25
        
        trackH = 0.125
        
        trackToolBar = TrackToolBar(self, (0, 0), (-1, trackH))

        trackY = trackToolBar.getBottom()
        toolZone = Frame((0, trackY), size=(separator, -1), parent=self)
        partZone = PartZone(instance, pos=(separator, trackY), size=(1 - separator, -1), parent=self)
        
        trackY = 0

        partZoneWidth, partZoneHeight = partZone.getSize()


        for track in instance.tracks:
            if (track != "length"):
                trackTool = TrackTool(track, toolZone, (0, trackY), (-1, trackH))
                trackPart = TrackPart(track, instance, partZone, (0, trackY), (-1, trackH), partZone.horizontalLineTexture)

                trackY += trackH


