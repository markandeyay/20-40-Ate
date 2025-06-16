import pygame

def draw_text(surface, text, pos, color=(255, 255, 255), size=20):
    font = pygame.font.SysFont("Arial", size)
    label = font.render(text, True, color)
    surface.blit(label, pos)

class Button:
    def __init__(self, rect, text, callback):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        self.color = (200, 200, 200)

    def draw(self, surface):
        draw_text(surface, self.text, (self.rect.x + 10, self.rect.y + 10))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()
