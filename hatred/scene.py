import pygame, app

class Scene:
    def __init__(self):
        self.loaded = False

    def on_load(self):
        pass

    def on_unload(self):
        pass

    def update(self, delta_time: float, _app: app.App):
        pass

    def render(self, surface: pygame.Surface, _app: app.App):
        pass