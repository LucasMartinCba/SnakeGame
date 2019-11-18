import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cubo(object):
    filas = 0
    ancho = 0

    def __init__(self, inicio, dirx=1, diry=0, color=(255, 0, 0)):
        pass

    def mover(self, dirx, diry):
        pass

    def dibujar(self, surface, eyes=False):
        pass


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
        pass

    def reset(self, pos):
        pass

    def addCubo(self):
        pass

    def dibujar(self, sup):
        pass


def dibujarGrid(ancho, filas, sup):
    tamaño = ancho // filas
    x = 0
    y = 0
    for i in range(filas):
        x += tamaño
        y += tamaño
        pygame.draw.line(sup, (255, 255, 255), (x, 0), (x, ancho))
        pygame.draw.line(sup, (255, 255, 255), (0, y), (ancho, y))


def reDibujarVentana(sup):
    global filas, ancho
    sup.fill((0, 0, 0))
    dibujarGrid(ancho, filas, sup)
    pygame.display.update()


def randomComida(filas, items):
    pass


def message_box(asunto, contenido):
    pass


def main():
    global ancho, filas
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
