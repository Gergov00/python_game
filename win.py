from config import *
import pygame as pg
import time
from krestiknolik import *


def winner(zapolneniekrestick, zapolnenienolick):
    if 1 in zapolneniekrestick and 4 in zapolneniekrestick and 7 in zapolneniekrestick:
        gorizont_rect.centery = 125
        screen.blit(gorizont, gorizont_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinkrestick, textwinkrestick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 2 in zapolneniekrestick and 5 in zapolneniekrestick and 8 in zapolneniekrestick:
        gorizont_rect.centery = 375
        screen.blit(gorizont, gorizont_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinkrestick, textwinkrestick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 3 in zapolneniekrestick and 6 in zapolneniekrestick and 9 in zapolneniekrestick:
        gorizont_rect.centery = 625
        screen.blit(gorizont, gorizont_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinkrestick, textwinkrestick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 1 in zapolneniekrestick and 2 in zapolneniekrestick and 3 in zapolneniekrestick:
        vertikal_rect.centerx = 130
        screen.blit(vertikal, vertikal_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinkrestick, textwinkrestick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 4 in zapolneniekrestick and 5 in zapolneniekrestick and 6 in zapolneniekrestick:
        vertikal_rect.centerx = 380
        screen.blit(vertikal, vertikal_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinkrestick, textwinkrestick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 7 in zapolneniekrestick and 8 in zapolneniekrestick and 9 in zapolneniekrestick:
        vertikal_rect.centerx = 630
        screen.blit(vertikal, vertikal_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinkrestick, textwinkrestick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 7 in zapolneniekrestick and 5 in zapolneniekrestick and 3 in zapolneniekrestick:
        screen.blit(vlevo, vlevo_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinkrestick, textwinkrestick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 1 in zapolneniekrestick and 5 in zapolneniekrestick and 9 in zapolneniekrestick:
        screen.blit(vpravo, vpravo_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinkrestick, textwinkrestick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 1 in zapolnenienolick and 4 in zapolnenienolick and 7 in zapolnenienolick:
        gorizont_rect.centery = 125
        screen.blit(gorizont, gorizont_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif (2 in zapolnenienolick and 5 in zapolnenienolick and 8 in zapolnenienolick):
        gorizont_rect.centery = 375
        screen.blit(gorizont, gorizont_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 3 in zapolnenienolick and 6 in zapolnenienolick and 9 in zapolnenienolick:
        gorizont_rect.centery = 625
        screen.blit(gorizont, gorizont_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 1 in zapolnenienolick and 2 in zapolnenienolick and 3 in zapolnenienolick:
        vertikal_rect.centerx = 130
        screen.blit(vertikal, vertikal_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 4 in zapolnenienolick and 5 in zapolnenienolick and 6 in zapolnenienolick:
        vertikal_rect.centerx = 380
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 7 in zapolnenienolick and 8 in zapolnenienolick and 9 in zapolnenienolick:
        vertikal_rect.centerx = 630
        screen.blit(vertikal, vertikal_rect)
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 7 in zapolnenienolick and 5 in zapolnenienolick and 3 in zapolnenienolick:
        screen.blit(vlevo, vlevo_rect)
        pg.display.update()
        time.sleep(1)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.fill(white)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif 1 in zapolnenienolick and 5 in zapolnenienolick and 9 in zapolnenienolick:
        screen.blit(vpravo, vpravo_rect)
        pg.display.update()
        time.sleep(1)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.fill(white)
        screen.blit(textwinnolick, textwinnolick_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)
    elif len(zapolneniekrestick)+len(zapolnenienolick) == 9:
        pg.display.update()
        time.sleep(1)
        screen.fill(white)
        screen.blit(textnichia, textnichia_rect)
        screen.blit(textquit, textquit_rect)
        screen.blit(textplayagain, textplayagain_rect)


