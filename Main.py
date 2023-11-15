import pygame as pg
from pygame.locals import *
from win import *
from config import *
from krestiknolik import *


ekran(white, black)






pg.display.update()
run = True
while True:
    cout = 0
    mas = []
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        elif event.type == pg.locals.MOUSEBUTTONUP:
            polojeniex, polojeniey = pg.mouse.get_pos()
            main(polojeniex, polojeniey, i, zapolneniekrestick, zapolnenienolick, mas)
            cout += 1
            if cout % 2 == len(mas) % 2:
                if i == 0:
                    i = 1
                else:
                    i = 0
            winner(zapolneniekrestick, zapolnenienolick)
            pg.display.update()
        elif event.type == pg.KEYUP:
            zapolneniekrestick = []
            zapolnenienolick = []
            if event.key == pg.K_p:
                ekran(white, black)
                i = 0
            if event.key == pg.K_q:
                pg.quit()
                break
    clock.tick(FPS)


