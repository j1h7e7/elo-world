import pygame
import math
size = (500, 500)
white_square=(230,250,230)
black_square=(40,80,40)
board_start=[50,50]
square_size=50

class Renderer:

    def __init__(self,screen):
        self.font = pygame.font.Font(None,50)
        self.p0 = pygame.transform.scale(pygame.image.load('pieces/p0.png'),(square_size,square_size))
        self.p1 = pygame.transform.scale(pygame.image.load('pieces/p1.png'),(square_size,square_size))
        self.n0 = pygame.transform.scale(pygame.image.load('pieces/n0.png'),(square_size,square_size))
        self.n1 = pygame.transform.scale(pygame.image.load('pieces/n1.png'),(square_size,square_size))
        self.b0 = pygame.transform.scale(pygame.image.load('pieces/b0.png'),(square_size,square_size))
        self.b1 = pygame.transform.scale(pygame.image.load('pieces/b1.png'),(square_size,square_size))
        self.r0 = pygame.transform.scale(pygame.image.load('pieces/r0.png'),(square_size,square_size))
        self.r1 = pygame.transform.scale(pygame.image.load('pieces/r1.png'),(square_size,square_size))
        self.q0 = pygame.transform.scale(pygame.image.load('pieces/q0.png'),(square_size,square_size))
        self.q1 = pygame.transform.scale(pygame.image.load('pieces/q1.png'),(square_size,square_size))
        self.k0 = pygame.transform.scale(pygame.image.load('pieces/k0.png'),(square_size,square_size))
        self.k1 = pygame.transform.scale(pygame.image.load('pieces/k1.png'),(square_size,square_size))

        self.pieces = {
            'P': self.p0,
            'p': self.p1,
            'N': self.n0,
            'n': self.n1,
            'B': self.b0,
            'b': self.b1,
            'R': self.r0,
            'r': self.r1,
            'Q': self.q0,
            'q': self.q1,
            'K': self.k0,
            'k': self.k1,
        }

        self.screen = screen

    def drawboard(self):
        for i in range(8):
            for j in range(8):
                color = white_square if (i+j)%2==0 else black_square
                pygame.draw.rect(self.screen,color,[board_start[0]+i*square_size,board_start[1]+j*square_size,square_size,square_size])

        for i in range(8):
            t1=self.font.render('ABCDEFGH'[i],True,(0,0,0))
            t2=t1.get_rect()
            t2.center=(board_start[0]+(i+0.5)*square_size,board_start[1]-0.5*square_size)
            self.screen.blit(t1,t2)
            t2.center=(board_start[0]+(i+0.5)*square_size,board_start[1]+8.5*square_size)
            self.screen.blit(t1,t2)

        for j in range(8):
            t1=self.font.render(str(j+1),True,(0,0,0))
            t2=t1.get_rect()
            t2.center=(board_start[0]-0.5*square_size,board_start[1]+(7.5-j)*square_size)
            self.screen.blit(t1,t2)
            t2.center=(board_start[1]+8.5*square_size,board_start[1]+(7.5-j)*square_size)
            self.screen.blit(t1,t2)

    def renderpieces(self, position):
        if type(position) is str:
            position = position.split(' ')[0]
            for i in range(1,9):
                position=position.replace(str(i)," "*i)
            position = position.split('/')
            position = [[x for x in s] for s in position]

        for i in range(8):
            for j in range(8):
                if(position[j][i]==' '): continue
                self.screen.blit(self.pieces[position[j][i]],[board_start[0]+i*square_size,board_start[1]+j*square_size])

    def findsquare(self,pos):
        boardpos = [math.floor((pos[i]-board_start[i])/square_size) for i in range(2)]

        if max(boardpos)>7 or min(boardpos)<0: return "N/A"

        return "abcdefgh"[boardpos[0]]+str(8-boardpos[1])