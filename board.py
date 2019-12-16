import pygame
import math
import drawboard

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode(drawboard.size)
render = drawboard.Renderer(screen)
pygame.display.set_caption("Testing")
clock = pygame.time.Clock()

position = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

startpos, endpos = "", ""

def move(sp, ep):
    s1 = 8-int(sp[1])
    s2 = "abcdefgh".index(sp[0])
    e1 = 8-int(ep[1])
    e2 = "abcdefgh".index(ep[0])

    position[s1][s2],position[e1][e2] = position[e1][e2],position[s1][s2]

running = True
while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type==pygame.QUIT: running=False

        if event.type == pygame.MOUSEBUTTONDOWN: startpos=render.findsquare(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            endpos = render.findsquare(pygame.mouse.get_pos())
            if not startpos=="N/A" and not endpos=="N/A": move(startpos,endpos)

    render.drawboard()
    render.renderpieces(position)

    pygame.display.flip()

    clock.tick(60)
