import pygame
import time

#Sound play logic
def Sound(file, volume, times):
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(times)
