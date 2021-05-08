from typing import Tuple, List

import pygame
from pygame import gfxdraw

from cube import Cube
from utils import colors, calculate_distance
from ray_tracing import trace

WIDTH = 800
HEIGHT = 600

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Cube")
clock = pygame.time.Clock()


def render_fps(screen: pygame.display, clock: pygame.time.Clock):
    font = pygame.font.SysFont(None, 24)
    fps = font.render('FPS: {:.2f}'.format(
        clock.get_fps()), True, colors['green'])
    screen.blit(fps, (20, 20))


def get_coords(first_coord: Tuple[float, float, float]) -> Tuple[float, float]:
    global WIDTH, HEIGHT
    return first_coord[0] + WIDTH // 2, first_coord[2] + HEIGHT // 2


def draw_cube(cube: Cube) -> None:
    for first_node in cube.nodes:
        for second_node in cube.nodes:
            if (int(calculate_distance(first_node, second_node)) - 200) <= 2:
                first_coords, second_coords = get_coords(
                    first_node), get_coords(second_node)
                pygame.draw.line(
                    screen, colors['white'], first_coords, second_coords)


def draw_plane(plane_nodes: List[Tuple[float, float, float]], color: str) -> None:
    pygame.draw.polygon(screen, colors[color], [
        get_coords(node) for node in plane_nodes])


cube = Cube()
cube.rotate(-30, 0, 60)

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
        rotation[0] = 1
    if keys[pygame.K_DOWN]:
        rotation[0] = -1
    cube.rotate(*rotation)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(colors['black'])
    draw_cube(cube)
    number = trace((0, 0), cube)
    point = get_coords((0, 0, 0))
    gfxdraw.pixel(screen, *point, colors['red'])
    draw_plane(cube.get_plane_coords(number), 'red')
    # for x in range(-100, 100, 10):
        # if x % 10 == 0:
        #     print(x)
        # for y in range(-100, 100, 10):
        #     number = trace((x, y), cube)
        #     if number != -1:
        #         point = get_coords((x, 0, y))
        #         draw_plane(cube.get_plane_coords(number), 'red')
                # gfxdraw.pixel(screen, *point, colors['red'])
    render_fps(screen, clock)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
