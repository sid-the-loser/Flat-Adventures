import pygame

pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Testing")

running = True

while running:
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), (0, 0, 75, 75))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False