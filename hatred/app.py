import pygame, settings, scene

pygame.init()

class App:
    def __init__(self):
        self.window = pygame.display.set_mode(settings.WINDOW_SIZE)
        pygame.display.set_caption(settings.WINDOW_TITLE)
        # pygame.display.set_icon(pygame.image.load("assets/icon.png"))
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = settings.FPS
        self.current_scene = None

    def get_window_surface(self):
        return self.window

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            delta_time = self.clock.get_time() / 1000.0

            if self.current_scene is not None:
                self.current_scene.update(delta_time)
                self.current_scene.render(self.window)

            self.window.fill(settings.WINDOW_BACKGROUND)

            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()

    def change_scene(self, new_scene: scene.Scene):
        if self.current_scene is not None:
            self.current_scene.on_unload()
            self.current_scene.loaded = False

        self.current_scene = new_scene

        if not self.current_scene.loaded:
            self.current_scene.on_load()
            self.current_scene.loaded = True