import pygame
from pygame import *


class Button:
    def __init__(self, title: str, size: tuple[int, int], color=Color(155, 230, 250), screen: display = None,
                 font=None) -> None:
        self.title = title
        self.size = size
        self.color = color
        self.rect = Rect((0, 0), size)
        self.on_click = None
        self.show = True
        self._screen = screen
        self._fonf = font

    def add_click_listener(self, func):
        self.on_click = func

    def render(self, surface: Surface, pos):
        if (not self.show):
            return
        self.rect.topleft = pos

        title_srf = self._fonf.render(self.title, True, Color(70, 50, 111))
        title_rect = title_srf.get_rect(center=self.rect.center)
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(title_srf, title_rect)

    def check(self):
        if self.on_click != None:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                clicked, _, _ = pygame.mouse.get_pressed()
                if clicked:
                    self.on_click()


