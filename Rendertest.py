import sys
import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Render Test")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)
text = font.render("Pygame is working! Press ESC or close window.", True, (255, 255, 255))
text_rect = text.get_rect(center=(WIDTH // 2, 40))

running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    angle = (angle + 2) % 360
    screen.fill((30, 30, 40))

    # Draw a rotating rectangle and a circle
    rect_size = 200
    rect_surface = pygame.Surface((rect_size, rect_size), pygame.SRCALPHA)
    pygame.draw.rect(rect_surface, (80, 180, 240, 180), rect_surface.get_rect(), border_radius=24)
    rotated = pygame.transform.rotozoom(rect_surface, angle, 1.0)
    rotated_rect = rotated.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rotated, rotated_rect)

    pygame.draw.circle(screen, (220, 220, 100), (WIDTH // 2, HEIGHT // 2), 80, 8)
    pygame.draw.circle(screen, (255, 120, 120), (WIDTH // 2, HEIGHT // 2), 16)

    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit(0)
