import math
import random
import pygame
import numpy as np

pygame.init()
W = 800
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("CompGr_Lab3_1")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()


def task1_1():
    x1 = random.randint(0, W)
    y1 = random.randint(0, H)
    x2 = random.randint(0, W)
    y2 = random.randint(0, H)
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx * dx + dy * dy)
    while length < 10:
        x1 = random.randint(0, W)
        y1 = random.randint(0, H)
        x2 = random.randint(0, W)
        y2 = random.randint(0, H)
        dx = x2 - x1
        dy = y2 - y1
        length = math.sqrt(dx * dx + dy * dy)
    sc.fill(WHITE)
    pygame.draw.circle(sc, (255, 255, 0), (x1, y1), 3)
    pygame.draw.circle(sc, (255, 255, 0), (x2, y2), 3)
    k = dy / dx
    if math.fabs(k) < 1:
        if x1 > x2:
            b = (x1, y1)
            x1, y1 = x2, y2
            x2, y2 = b
        x = x1
        y = y1
        while x < x2:
            pygame.draw.rect(sc, BLACK, (x, y, 1, 1))
            y += k
            x += 1
    else:
        if y1 > y2:
            b = (x1, y1)
            x1, y1 = x2, y2
            x2, y2 = b
        x = x1
        y = y1
        while y < y2:
            pygame.draw.rect(sc, BLACK, (x, y, 1, 1))
            x += 1 / k
            y += 1
    pygame.display.update()
    print(f"{x1},{y1} and {x2},{y2}. k = {k}")


def task1_2():
    x1 = random.randint(0, W)
    y1 = random.randint(0, H)
    x2 = random.randint(0, W)
    y2 = random.randint(0, H)
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx * dx + dy * dy)
    while length < 10:
        x1 = random.randint(0, W)
        y1 = random.randint(0, H)
        x2 = random.randint(0, W)
        y2 = random.randint(0, H)
        dx = x2 - x1
        dy = y2 - y1
        length = math.sqrt(dx * dx + dy * dy)
    sc.fill(WHITE)
    pygame.draw.circle(sc, (255, 255, 0), (x1, y1), 3)
    pygame.draw.circle(sc, (255, 255, 0), (x2, y2), 3)
    if math.fabs(dy / dx) < 1:
        if x1 > x2:
            b = (x1, y1)
            x1, y1 = x2, y2
            x2, y2 = b
        x = x1
        y = y1
        sc.set_at((x, y), BLACK)
        x += 1
        while x < x2:
            if not((y-1/2-y1)/(x-x1) < (y2-y1)/(x2-x1) < (y+1/2-y1)/(x-x1)):
                y += int(np.sign((y2-y1)/(x2-x1)))
            sc.set_at((x, y), BLACK)
            x += 1
    else:
        if y1 > y2:
            b = (x1, y1)
            x1, y1 = x2, y2
            x2, y2 = b
        x = x1
        y = y1
        sc.set_at((x, y), BLACK)
        y += 1
        while y < y2:
            if not ((y - y1) / (x + 1 / 2 - x1) < (y2 - y1) / (x2 - x1) < (y - y1) / (x - 1 / 2 - x1)):
                x += int(np.sign((y2 - y1) / (x2 - x1)))
            sc.set_at((x, y), BLACK)
            y += 1
    pygame.display.update()


def task2():
    r1 = random.randint(2, int(min(W / 2, H / 2)))
    r2 = random.randint(2, int(min(W / 2, H / 2)))
    x1 = random.randint(r1, W - r1)
    y1 = random.randint(r1, H - r1)
    x2 = random.randint(r2, W - r2)
    y2 = random.randint(r2, H - r2)
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx * dx + dy * dy)
    while length > r1 + r2:
        r1 = random.randint(2, int(min(W / 2, H / 2)))
        r2 = random.randint(2, int(min(W / 2, H / 2)))
        x1 = random.randint(r1, W - r1)
        y1 = random.randint(r1, H - r1)
        x2 = random.randint(r2, W - r2)
        y2 = random.randint(r2, H - r2)
        dx = x2 - x1
        dy = y2 - y1
        length = math.sqrt(dx * dx + dy * dy)
    sc.fill(WHITE)
    circle_bres(x1, y1, r1)
    circle_bres(x2, y2, r2)
    fill_circles(np.array([x1, y1]), r1, np.array([x2, y2]), r2)
    pygame.display.update()


def circle_bres(xc, yc, r):
    x, y = 0, r
    d = 3 - 2 * r
    draw_circle(xc, yc, x, y)
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        draw_circle(xc, yc, x, y)


def draw_circle(xc, yc, x, y):
    sc.set_at((xc + x, yc + y), BLACK)
    sc.set_at((xc - x, yc + y), BLACK)
    sc.set_at((xc + x, yc - y), BLACK)
    sc.set_at((xc - x, yc - y), BLACK)
    sc.set_at((xc + y, yc + x), BLACK)
    sc.set_at((xc - y, yc + x), BLACK)
    sc.set_at((xc + y, yc - x), BLACK)
    sc.set_at((xc - y, yc - x), BLACK)


def np_fill_line(COLOR, p, dy, preP):
    fill_line(COLOR, int(p[0]), int(p[1]), dy, int(preP[0]), int(preP[1]))


def fill_line(COLOR, x, y, dy, preXL, preXR):
    if not (0 < x < W) or not (0 < y < H):
        return
    xl = x
    xr = x
    c = (0, 0, 0)
    c = sc.get_at((x, y))[0:3]
    while (c != BLACK) and (xl > 0):
        xl -= 1
        c = sc.get_at((xl, y))[0:3]

    c = sc.get_at((xr, y))[0:3]
    while (c != BLACK) and (xr < W - 1):
        xr += 1
        c = sc.get_at((xr, y))[0:3]
    # print(f"{xl},{xr}. y={y}")
    if xl == xr:
        return x
    xl += 1
    xr -= 1
    pygame.draw.rect(sc, COLOR, (xl, y, xr - xl + 1, 1))
    if H > y + dy > 0:
        x_iter = xl
        while x_iter < xr + 1 and x_iter < W:
            c = sc.get_at((x_iter, y + dy))[0:3]
            if (c != BLACK) and (c != COLOR):
                x_iter = fill_line(COLOR, x_iter, y + dy, dy, xl, xr)
            x_iter += 1
    if H > y - dy > 0 and preXL > 0:
        x_iter = xl
        while x_iter < xr + 1 and x_iter < W:
            c = sc.get_at((x_iter, y - dy))[0:3]
            if (sc.get_at((x_iter, y))[0:3] == COLOR) and ((c != BLACK) and (c != COLOR)):
                x_iter = fill_line(COLOR, x_iter, y - dy, -dy, -1, -1)
            x_iter += 1
    return xr


def fill_circles(c1, r1, c2, r2):
    length = np.sqrt(np.sum((c1-c2)*(c1-c2)))
    b1 = c1 + r1 * (c1 - c2) / length
    b2 = c1 - r1 * (c1 - c2) / length
    d1 = c2 + r2 * (c1 - c2) / length
    d2 = c2 - r2 * (c1 - c2) / length
    # print(b1, b2, d1, d2)
    i = 0
    if (int(b1[0]) - int(d1[0]))*(int(b2[0]) - int(d2[0])) == 0:
        i = 1
    if (b1[i] - d1[i])*(b2[i] - d2[i]) > 0:
        np_fill_line(RED, (b1 + d1) / 2, 1, -np.ones(2))
        np_fill_line(RED, (b1 + d1) / 2, -1, -np.ones(2))
        np_fill_line(BLUE, (b2 + d2) / 2, 1, -np.ones(2))
        np_fill_line(BLUE, (b2 + d2) / 2, -1, -np.ones(2))
        np_fill_line(GREEN, (d1 + b2) / 2, 1, -np.ones(2))
        np_fill_line(GREEN, (d1 + b2) / 2, -1, -np.ones(2))
    else:
        if r1 > r2:
            np_fill_line(RED, (b1 + d1) / 2, 1, -np.ones(2))
            np_fill_line(RED, (b1 + d1) / 2, -1, -np.ones(2))
            np_fill_line(GREEN, (d1 + d2) / 2, 1, -np.ones(2))
            np_fill_line(GREEN, (d1 + d2) / 2, -1, -np.ones(2))
            np_fill_line(RED, (b2 + d2) / 2, 1, -np.ones(2))
            np_fill_line(RED, (b2 + d2) / 2, -1, -np.ones(2))
        else:
            np_fill_line(BLUE, (b1 + d1) / 2, 1, -np.ones(2))
            np_fill_line(BLUE, (b1 + d1) / 2, -1, -np.ones(2))
            np_fill_line(GREEN, (b1 + b2) / 2, 1, -np.ones(2))
            np_fill_line(GREEN, (b1 + b2) / 2, -1, -np.ones(2))
            np_fill_line(BLUE, (b2 + d2) / 2, 1, -np.ones(2))
            np_fill_line(BLUE, (b2 + d2) / 2, -1, -np.ones(2))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                task1_1()
            elif event.key == pygame.K_q:
                task1_2()
            elif event.key == pygame.K_2:
                task2()
    clock.tick(FPS)
