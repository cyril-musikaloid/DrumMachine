from button import *
import frame

toolbarSize = 0.05

def quitRelease(self:Button, instance, hitPos):
    if self.hitTest(hitPos):
        instance.running = False

def leftCB(self:Button, instance, hitPos):
    if self.hitTest(hitPos):
        instance.timestampToStart()

def rightCB(self:Button, instance, hitPos):
    if self.hitTest(hitPos):
        instance.timestamp -= 13

class Toolbar(frame.Frame):
    def __init__(self, parent):
        super().__init__(parent=parent)

        parentW, parentH = parent.getSize()
        self._size = (parentW, int(toolbarSize * parentH))

        quitSize = (int(toolbarSize * parentH), int(toolbarSize * parentH))
        quitButton = Button((-toolbarSize * parentW, 0), quitSize,self, Texture("quitPress.svg", quitSize), Texture("quitRelease.svg", quitSize))
        quitButton.setReleaseCallback(quitRelease)

        leftOffset = Button(pos=(0, 0),size=quitSize, parent = self, pressTexture=ColorTexture(67, 98,167, quitSize),
                            releaseTexture=ColorTexture(176,87,2, quitSize))
        
        rightOffset = Button(pos=(leftOffset.getRight() + 10, 0), size=quitSize, parent = self, pressTexture=ColorTexture(67, 98,167, quitSize),
                            releaseTexture=ColorTexture(176,87,2, quitSize))
        
        leftOffset.setReleaseCallback(leftCB)
        rightOffset.setReleaseCallback(rightCB)
        