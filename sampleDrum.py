import pygame.mixer as mx
import json

def init():
    mx.init(channels=16)

class SampleDrum:

    def __init__(self, drumName = "Default.json"):
        with open("./Sample/"+drumName) as drumFile:
            jsonData = drumFile.read()
            self.sampleFileList = json.loads(jsonData)

        self.soundList = {
            "kick": {
                "sound":mx.Sound("./Sample/"+self.sampleFileList["kick"]),
                "channel":mx.Channel(1)
            },
            "clap": {
                "sound":mx.Sound("./Sample/"+self.sampleFileList["ridclap"]),
                "channel":mx.Channel(2)
            }
        }

    def play(self, sample: str):
        self.soundList[sample]["channel"].play(self.soundList[sample]["sound"])
