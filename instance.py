class Instance():
    def __init__(self, trackZoom = 1, numberDisplayedStep = 8, drum = None, window = None, tempo = 90,
                 timestamp=-1, tempoDiv=2):
        self.trackZoom = trackZoom
        self.numberDisplayedStep = numberDisplayedStep / trackZoom
        self.drum = drum
        self.window = window
        self.running = True
        self.tracks = {
            "length": 8,
            "kick": {1, 3, 5},
            "clap": {0}
        }
        self.tempo = tempo
        self.tempoDiv = tempoDiv
        if timestamp < 0:
            self.timestamp = self.getStartTimestamp()
        else:
            self.timestamp = timestamp
        self.isPlaying = False
        self.shouldRenderTempoDiv = True
        self.lastStep = -1

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def getStepDurationMS(self):
        return int(60 / self.tempo * 1000)
    
    def increaseTimeStamp(self, dt):
        self.timestamp += dt

    def getStep(self):
        return int((self.timestamp - self.getStartTimestamp()) / self.getStepDurationMS() - (1.0 if self.timestamp < 0 else 0.0))

    def execute(self):
        step = self.getStep()

        if (step != self.lastStep):
            print(self.getStepDurationMS())
            self.lastStep = step

            for track in self.tracks:
                if track != "length":
                    if step in self.tracks[track]:
                        self.drum.play(track)

    def getStartTimestamp(self):
        return 0#int(-self.getStepDurationMS() / 2)
    
    def timestampToStart(self):
        self.timestamp = self.getStartTimestamp()

    def timestampToLastNote(self):
        lastNotePos = 0

        for track in self.tracks:
            if track != "length":
                maxNotePos = max(self.tracks[track])

                if maxNotePos > lastNotePos:
                    lastNotePos = maxNotePos

        self.timestamp = self.getStepDurationMS() * lastNotePos - self.getStepDurationMS() * (self.numberDisplayedStep-1)



    def setTempoDiv(self, tempoDiv):
        self.tempoDiv = tempoDiv

    def setTrackZoom(self, trackZoom):
        self.trackZoom = trackZoom
        self.numberDisplayedStep = 8 / trackZoom

    def getTimestamp(self):
        return self.timestamp