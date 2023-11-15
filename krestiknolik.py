import pygame as pg
from config import *
i = 0
def main(polojeniex, polojeniey, i, zapolneniekrestick, zapolnenienolick, mas):
    x, y, coux, couy = 250, 250, 0, 1
    while polojeniex > x:
        x += 250
        coux += 1
    while polojeniey > y:
        y += 250
        couy += 1
    petuh = coux * 3 + couy
    if i == 0:
        if petuh not in zapolnenienolick:
            krestik_rect.center = (x - 125, y - 125)
            screen.blit(krestik, krestik_rect)
            zapolneniekrestick.append(petuh)
            mas.append(0)
    else:
        if petuh not in zapolneniekrestick:
            nolick_rect.center = (x - 125, y - 125)
            screen.blit(nolick, nolick_rect)
            zapolnenienolick.append(petuh)
            mas.append(0)


def ekran(white, black):
    screen.fill(white)
    for y in range(3):
        for x in range(3):
            pg.draw.rect(screen, black, (x * 250, y * 250, 250, 250), 2)
            pg.display.update()