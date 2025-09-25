import pygame

class Scene:
    def __init__(self):
        self.loaded = False

    def on_load(self):
        pass

    def on_unload(self):
        pass

    def update(self, delta_time: float):
        pass

    def render(self, surface: pygame.Surface):
        pass