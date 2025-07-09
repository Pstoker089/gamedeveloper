import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))

class circle:
    def __init__(self,colour,position,radius):
        self.colour=colour
        self.position=position
        self.radius=radius
        self.screen=screen
    def display(self):
        pygame.draw.circle(self.screen,self.colour,self.position,self.radius)
    def grow(self):
        self.radius+=10
        pygame.draw.circle(self.screen,self.colour,self.position,self.radius)


c1=circle("red",(300,300),10)
c2=circle("green",(300,300),4)
c3=circle("yellow",(300,300),2)
c4=circle("red",(300,300),1)




screen.fill("White")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            c1.display()
            c2.display()
            c3.display()
            c4.display()
        elif event.type==pygame.MOUSEBUTTONUP:
            c1.grow()
            c2.grow()
            c3.grow()
            c4.grow()
        elif event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            c5=circle("black",pos,1)
            c5.display()
    

    pygame.display.update()