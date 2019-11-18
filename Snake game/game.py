import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cubo(object):
    filas = 20
    ancho = 500

    def __init__(self, inicio, dirx=1, diry=0, color=(255, 0, 0)):
        self.pos = inicio
        self.dirx = dirx
        self.diry = diry
        self.color = color

    def mover(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos(self.pos[0] + self.dirx, self.pos[1] + self.diry)

    def dibujar(self, sup, ojos=False):
        dis = self.ancho // self.filas
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(sup, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))




class snake(object):
    cuerpo = []
    mov = []

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
            # Controles
            for key in keys:
                if key[pygame.K_LEFT]:
                    self.dirx = -1
                    self.diry = 0
                    self.mov[self.cabeza.pos[:]] = [self.dirx, self.diry]
                elif key[pygame.K_RIGHT]:
                    self.dirx = 1
                    self.diry = 0
                    self.mov[self.cabeza.pos[:]] = [self.dirx, self.diry]
                elif key[pygame.K_UP]:
                    self.dirx = 0
                    self.diry = -1
                    self.mov[self.cabeza.pos[:]] = [self.dirx, self.diry]
                elif key[pygame.K_DOWN]:
                    self.dirx = 0
                    self.diry = -1
                    self.mov[self.cabeza.pos[:]] = [self.dirx, self.diry]

        for i, c in enumerate(self.cuerpo):
            p = c.pos[:]
            if p in self.mov:
                mov = self.mov[p]
                c.mover(mov[0], mov[i])
                # Elimina el ultimo cubo
                if i == len(self.cuerpo) - 1:
                    self.mov.pop(p)

                # Chequear el final de la pantalla
                else:

                    # Si se mueve hacia la izquierda y la posicion x es menor o igual a 0(borde izquierdo de la
                    # pantalla), se cambia la posicion hacia el borde derecho de la pantalla

                    if c.dirx == -1 and c.pos[0] <= 0:
                        c.pos = (c.filas - 1, c.pos[1])

                    # Si se mueve hacia la derecha y la posicion x es mayor o igual al borde de la pantalla, se cambia
                    # la posicion hacia el borde izquierdo

                    elif c.dirx == 1 and c.pos[0] >= c.filas - 1:
                        c.pos = (0, c.pos[1])
                    # Si se mueve hacia abajo y la posicion y es mayor o igual al borde inferior de la pantalla, se
                    # cambia la posicion hacia el superior
                    elif c.diry == 1 and c.pos[1] >= c.filas - 1:
                        c.pos = (c.pos[0], 0)

                    # Si se mueve hacia arriba y la posicion es menor o igual al borde superior de la pantalla,
                    # se cambia la posicion hacia el inferior.
                    elif c.diry == -1 and c.pos[1] <= 0:
                        c.pos = (c.pos[0], c.filas - 1)

                    # Si no sigue moviendose a la direccion que deberia
                    else:
                        c.mover(c.dirx, c.diry)

    def reset(self, pos):
        pass

    def addCubo(self):
        pass

    def dibujar(self, sup):
        for i, c in enumerate(self.cuerpo):
            if i == 0:
                c.dibujar(sup, True)
            else:
                c.dibujar(sup)


def dibujarGrid(ancho, filas, sup):
    tamanio = ancho // filas
    x = 0
    y = 0
    for i in range(filas):
        x += tamanio
        y += tamanio
        pygame.draw.line(sup, (255, 255, 255), (x, 0), (x, ancho))
        pygame.draw.line(sup, (255, 255, 255), (0, y), (ancho, y))


def reDibujarVentana(sup):
    global filas, ancho, s
    sup.fill((0, 0, 0))
    s.dibujar(sup)
    dibujarGrid(ancho, filas, sup)
    pygame.display.update()


def randomComida(filas, items):
    pass


def message_box(asunto, contenido):
    pass


def main():
    global ancho, filas, s
    ancho = 500
    filas = 20
    ventana = pygame.display.set_mode((ancho, ancho))
    s = snake((255, 0, 0), (10, 10))
    flag = True
    reloj = pygame.time.Clock()
    while flag:
        # Control de velocidad de juego
        pygame.time.delay(50)
        reloj.tick(10)

        reDibujarVentana(ventana)


main()
