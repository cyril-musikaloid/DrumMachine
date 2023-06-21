

class DummyTexture():
    def __init__(self):
        pass

    def _getSurface(self):
        return None

    def _render(self, surface = None, pos  =(0,0)):
        pass

class Frame():
    def __init__(self, pos = (0, 0), size = (0,0), parent = None, addParentChild = True, texture = DummyTexture):
        self.parent = parent
        self._pos = pos
        self._size = size
        if (not hasattr(self, "_texture")):
            self._texture = texture
        self._child = []
        if (parent != None and addParentChild):
            parent.addChild(self)

    def setPosistion(self, pos):
        self._pos = pos

    def setSize(self, size):
        self._size = size

    def getSize(self):
        w, h = self._size

        if (self.parent != None):
            parentWidth, parentHeight = self.parent.getSize()

            if (type(w) is float):
                w *= parentWidth

            if (type(h) is float):
                h *= parentHeight

            if (w < 0):
                w = parentWidth

            if (h < 0):
                h = parentHeight

        return (int(w), int(h))
    
    def getPosition(self, absolute = False):
        x, y = self._pos
        w, h = self.getSize()
        
        if (self.parent != None):
            parentSize, parentHeigh = self.parent.getSize()

            if (type(x) is float):
                x *= parentSize

            if (type(y) is float):
                y *= parentHeigh

            if (x < 0):
                x = parentSize - w

            if (y < 0):
                y = parentHeigh - h

            if (absolute):
                parentX, parentY = self.parent.getPosition(True)
                x += parentX
                y += parentY

        return (int(x), int(y))
    
    def globalToLocal(self, pos = (0, 0)):
        x, y = self.getPosition(True)
        posX, posY = pos

        return (posX - x, posY - y)
    
    def getBottom(self):
        x, y = self.getPosition()
        w, h = self.getSize()

        return y + h
    
    def getTop(self):
        x, y = self.getPosition()
        w, h = self.getSize()

        return y
    
    def getLeft(self):
        x, y = self.getPosition()
        w, h = self.getSize()

        return x
    
    def getRight(self):
        x, y = self.getPosition()
        w, h = self.getSize()

        return x + w

    def getWidth(self):
        w, h = self.getSize()

        return w
    
    def getHeight(self):
        w, h = self.getSize()

        return h

    def setTexture(self, texture):
        self._texture = texture

    def getTexture(self):
        return self._texture

    def addChild(self, frame):
        self._child.append(frame)

    def render(self, window):
        for frame in self._child:
            window.render(frame)

    def hitTest(self, pos):
        hitX, hitY = pos
        frameX, frameY = self.getPosition(True)
        frameW, frameH = self.getSize()

        if (hitX >= frameX and hitX <= frameX + frameW and hitY >= frameY and hitY <= frameY + frameH):
            return True
        return False

    def fingerDown(self, instance, pos = (0,0)):
        for frame in self._child:
            if (frame.hitTest(pos)):
                frame.fingerDown(instance, pos)

    def fingerUp(self, instance, pos = (0,0)):
        for frame in self._child:
            frame.fingerUp(instance, pos)

    def setParent(self, parent = None):
        if self.parent != None:
            self.parent.removeChild(self)

        self.parent = parent

        if parent != None:
            parent.addChild(self)

    def removeChild(self, child):
        self._child.remove(child)
