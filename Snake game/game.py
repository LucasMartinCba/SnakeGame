import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
pygame.init()
pygame.display.set_caption("Snake Game")

class cubo(object):
    filas = 20
    a = 500

    def __init__(self, start, dirx=1, diry=0, color=(255,255,255)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.color = color

    def mover(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)

    def dibujar(self, sup, ojos=False):
        dis = self.a // self.filas
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(sup, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if ojos:
            centre = dis // 2
            radio = 3
            ojo1 = (i * dis + centre - radio, j * dis + 8)
            ojo2 = (i * dis + dis - radio * 2, j * dis + 8)
            pygame.draw.circle(sup, (0, 0, 0), ojo1, radio)
            pygame.draw.circle(sup, (0, 0, 0), ojo2, radio)


class snake(object):
    cuerpo = []
    movs = {}

    def __init__(self, color, pos):
        self.color = color
        self.cabeza = cubo(pos)
        self.cuerpo.append(self.cabeza)
        self.dirx = 0
        self.diry = 1

    def mover(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirx = -1
                    self.diry = 0
                    self.movs[self.cabeza.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.movs[self.cabeza.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.movs[self.cabeza.pos[:]] = [self.dirx, self.diry]

                elif keys[pygame.K_DOWN]:
                    self.dirx = 0
                    self.diry = 1
                    self.movs[self.cabeza.pos[:]] = [self.dirx, self.diry]

        for i, c in enumerate(self.cuerpo):
            p = c.pos[:]
            if p in self.movs:
                mov = self.movs[p]
                c.mover(mov[0], mov[1])
                if i == len(self.cuerpo) - 1:
                    self.movs.pop(p)
            else:
                if c.dirx == -1 and c.pos[0] <= 0:
                    c.pos = (c.filas - 1, c.pos[1])
                elif c.dirx == 1 and c.pos[0] >= c.filas - 1:
                    c.pos = (0, c.pos[1])
                elif c.diry == 1 and c.pos[1] >= c.filas - 1:
                    c.pos = (c.pos[0], 0)
                elif c.diry == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.filas - 1)
                else:
                    c.mover(c.dirx, c.diry)

    def reset(self, pos):
        self.cabeza = cubo(pos)
        self.cuerpo = []
        self.cuerpo.append(self.cabeza)
        self.movs = {}
        self.dirx = 0
        self.diry = 1

    def addCubo(self):
        cola = self.cuerpo[-1]
        dx, dy = cola.dirx, cola.diry

        if dx == 1 and dy == 0:
            self.cuerpo.append(cubo((cola.pos[0] - 1, cola.pos[1])))
        elif dx == -1 and dy == 0:
            self.cuerpo.append(cubo((cola.pos[0] + 1, cola.pos[1])))
        elif dx == 0 and dy == 1:
            self.cuerpo.append(cubo((cola.pos[0], cola.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.cuerpo.append(cubo((cola.pos[0], cola.pos[1] + 1)))

        self.cuerpo[-1].dirx = dx
        self.cuerpo[-1].diry = dy

    def dibujar(self, surface):
        for i, c in enumerate(self.cuerpo):
            if i == 0:
                c.dibujar(surface, True)
            else:
                c.dibujar(surface)


def dibujarGrid(w, rows, surface):
    tamanio = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + tamanio
        y = y + tamanio

        pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, w))
        pygame.draw.line(surface, (0, 0, 0), (0, y), (w, y))


def reDibujarVentana(sup):
    global filas, ancho, s, snack
    sup.fill((0, 100, 0))
    s.dibujar(sup)
    snack.dibujar(sup)
    dibujarGrid(ancho, filas, sup)
    pygame.display.update()


def randomComida(f, item):
    posiciones = item.cuerpo

    while True:
        x = random.randrange(f)
        y = random.randrange(f)
        if len(list(filter(lambda z: z.pos == (x, y), posiciones))) > 0:
            continue
        else:
            break

    return (x, y)


def message_box(asunto, contenido):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(asunto, contenido)
    try:
        root.destroy()
    except:
        pass


def main():
    global ancho, filas, s, snack
    ancho = 500
    filas = 20
    win = pygame.display.set_mode((ancho, ancho))
    s = snake((255, 255, 255), (10, 10))
    snack = cubo(randomComida(filas, s), color= (255, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.mover()
        if s.cuerpo[0].pos == snack.pos:
            s.addCubo()
            snack = cubo(randomComida(filas, s), color= (255, 255, 0))

        for x in range(len(s.cuerpo)):
            if s.cuerpo[x].pos in list(map(lambda z: z.pos, s.cuerpo[x + 1:])):
                print('Score: ', len(s.cuerpo))
                message_box('You Lost!', 'Play again...')
                s.reset((10, 10))
                break

        reDibujarVentana(win)


main()
