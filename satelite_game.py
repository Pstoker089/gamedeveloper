import pgzrun
from random import randint
from time import time

satelites=[]

WIDTH=500
HEIGHT=500

lines=[]
currentsatelite=0
starttime=time()
timedifference=0
satelitecount=8


for i in range(8):
    satelite=Actor("satelite")
    satelite.pos=randint(50,450),randint(50,450)
    satelites.append(satelite)

def draw():
    global timedifference
    screen.blit("space",(0,0))
    number=1
    for i in satelites:
        i.draw()
        screen.draw.text(str(number),(i.pos[0]-10,i.pos[1]+20))
        number+=1
    if currentsatelite<satelitecount :
        timedifference=time()-starttime
        screen.draw.text(str(round(timedifference)),(10,10),fontsize=20)
    else:
        screen.draw.text(str(round(timedifference)),(10,10),fontsize=20)
    for i in lines:
        screen.draw.line(i[0],i[1],"white")
    


def update():
    pass

def on_mouse_down(pos):
    global currentsatelite
    global satelitecount
    global lines
    global satelites
    if currentsatelite<satelitecount :
        if satelites[currentsatelite].collidepoint(pos):
            if currentsatelite:
                lines.append((satelites[currentsatelite-1].pos,satelites[currentsatelite].pos))
            currentsatelite+=1
        else:
            currentsatelite=0
            lines=[]
                
    


pgzrun.go()





