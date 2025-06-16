import pygame
import sys
from src.utils import Button, draw_text
from src.audio import play_music, toggle_music
from src.game import run_game

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("20-40-Ate")

menu_music = "assets/music/menu_music.mp3"

def run_menu():
    from src.audio import music_on

    play_music(menu_music)

    clock = pygame.time.Clock()

    play_button = Button((225, 250, 150, 50), "Play", lambda: run_game())
    music_button = Button((520, 20, 60, 30), "Music" if music_on else "Mute", toggle_music)

    running = True
    while running:
        screen.fill((30, 30, 30))
        draw_text(screen, "20-40-Ate", (200, 100))
        draw_text(screen, "by Markandeya Yalamanchi", (160, 140))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play_button.check_click(event.pos)
                music_button.check_click(event.pos)

        play_button.draw(screen)
        music_button.text = "Music" if music_on else "Mute"
        music_button.draw(screen)

        pygame.display.flip()
        clock.tick(60)
