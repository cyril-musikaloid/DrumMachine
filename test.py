import pygame
import sampleDrum
import time
from frame import *
from pygameGraphic import *
from button import *
from toolbar import *
from padZone import *
from trackZone import *
from instance import *

#window = Window()
window = Window((1280, 720))

SCREEN_WIDTH, SCREEN_HEIGHT = window.getSize()

drum = sampleDrum.SampleDrum()

mainFrame = Frame((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))

mainBg = ColorTexture(200, 200, 75, (SCREEN_WIDTH, SCREEN_HEIGHT))
mainFrame.setTexture(mainBg)

toolbar = Toolbar(mainFrame)
instance = Instance(drum=drum, trackZoom=1, tempo=30)

padZone = PadZone(instance, mainFrame, (0, -1), (SCREEN_WIDTH, 0.33))

tZone = TrackZone(instance, mainFrame, size=(-1, 0.5), pos=(0, toolbar.getBottom()))

window.render(mainFrame)

pygame.display.flip()

clock = pygame.time.Clock()

fd = 0

while instance.running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #if event.type == pygame.FINGERDOWN:
        #    mainFrame.fingerDown(instance, (event.x * SCREEN_WIDTH, event.y * SCREEN_HEIGHT))
            #fd += 1

        #if event.type == pygame.FINGERUP:
        #    mainFrame.fingerUp(instance, (event.x * SCREEN_WIDTH, event.y * SCREEN_HEIGHT))

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            fd += 1
            mainFrame.fingerDown(instance, (x, y))

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            mainFrame.fingerUp(instance, (x, y))

        

    window.render(mainFrame)
    window.update()
    dt = clock.tick(60)

    if (instance.isPlaying):
        instance.increaseTimeStamp(dt)
        instance.execute()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        drum.play("kick")
    if keys[pygame.K_x]:
        time.sleep(0.02)
        drum.play("clap")
    if keys[pygame.K_c]:
        time.sleep(0.01)
        drum.play("clap")
    if keys[pygame.K_v]:
        time.sleep(0.005)
        drum.play("clap")    

print(fd)


