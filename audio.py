import pygame
import os

music_on = True

def play_music(track_path):
    if music_on:
        full_path = os.path.join(os.path.dirname(__file__), "..", track_path)
        pygame.mixer.music.load(full_path)
        pygame.mixer.music.play(-1)

def toggle_music():
    global music_on
    music_on = not music_on
    if music_on:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
