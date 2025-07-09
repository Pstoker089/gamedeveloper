#pygame mandatory stuff
import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))

class shape:
    def __init__(self,colour,size):
        self.colour=colour
        self.size=size
        self.screen=screen
    def display(self):
        pygame.draw.rect(self.screen,self.colour,self.size)

s1=shape("red",(200,200,100,100))
s2=shape("blue",(100,100,50,50))
s3=shape("green",(400,400,50,50))


#mandatory for pygame
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    screen.fill("White")
    s1.display()
    s2.display()
    s3.display()
    pygame.display.update()
