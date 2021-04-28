import pygame
from cube import Cube
from typing import Tuple

WIDTH = 800
HEIGHT = 600

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Cube")
clock = pygame.time.Clock()

colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'green': (0, 255, 0)
}


def calculate_distance(first_coords: Tuple[int, int, int], second_coords: Tuple[int, int, int]) -> float:
    return ((first_coords[0] - second_coords[0]) ** 2 + (first_coords[1] - second_coords[1]) ** 2 + (first_coords[2] - second_coords[2]) ** 2) ** (1/2)


def get_coords(first_coord: Tuple[int, int, int], second_coord: Tuple[int, int, int]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    global WIDTH, HEIGHT
    return (first_coord[0] + WIDTH // 2, first_coord[2] + HEIGHT // 2), (second_coord[0] + WIDTH // 2, second_coord[2] + HEIGHT // 2)


def draw_cube(cube: Cube) -> None:
    for first_node in cube.nodes:
        for second_node in cube.nodes:
            if (int(calculate_distance(first_node, second_node)) - 200) <= 2:
                coords = get_coords(first_node, second_node)
                pygame.draw.line(
                    screen, colors['white'], coords[0], coords[1])


cube = Cube()
print(type(cube))
cube.rotate(0, -30, 60)

FPS = 60
running = True
while running:
    keys = pygame.key.get_pressed()
    rotation = [0, 0, 0]
    if keys[pygame.K_RIGHT]:
        rotation[2] = 1
    if keys[pygame.K_LEFT]:
        rotation[2] = -1
    if keys[pygame.K_UP]:
        rotation[1] = 1
    if keys[pygame.K_DOWN]:
        rotation[1] = -1
    cube.rotate(*rotation)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(colors['black'])
    draw_cube(cube)
    font = pygame.font.SysFont(None, 24)
    fps = font.render('FPS: {:.2f}'.format(clock.get_fps()), True, colors['green'])
    screen.blit(fps, (20, 20))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
