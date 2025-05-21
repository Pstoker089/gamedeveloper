import pgzrun, random

WIDTH=1210
HEIGHT=908


startspeed=10
gamewin=False
gamelose=False
totallevel=6
currentlevel=1
animations=[]
everything=[]
bad=["bottle","chips","battery","bag"]

def draw():
    screen.blit("green_background",(0,0))
    if gamewin:
        screen.draw.text("YOU WIN",(600,450),fontsize=40, color="black")
    elif gamelose:
        screen.draw.text("YOU LOSE",(600,450),fontsize=40, color="black")  
    else:
        for i in everything:
            i.draw()

def update():
    global everything
    if len(everything)==0:
        everything=master(currentlevel)
        

def master(extraitems):
    stuff=stuffchoice(extraitems)
    actorstuff=actors(stuff)
    layout(actorstuff)
    animateitems(actorstuff)
    return actorstuff

def stuffchoice(extraitems):
    stuff=["paper"]
    for i in range(extraitems):
        itemchoice=random.choice(bad)
        stuff.append(itemchoice)
    return stuff

def actors(stuff):
    actorstuff=[]
    for i in stuff:
        image=Actor(i)
        actorstuff.append(image)
    return actorstuff

def layout(itemstolayout):
    numbgaps=len(itemstolayout)+1
    gapsize=WIDTH/numbgaps
    random.shuffle(itemstolayout)
    for i in itemstolayout:
        i.x=gapsize
        gapsize+=gapsize

def animateitems(itemstoanimate):
    for i in itemstoanimate:
        duration=startspeed-currentlevel
        i.anchor=("center","bottom")
        animated=animate(i,duration=duration,on_finished=finish(),y=HEIGHT)
        animations.append(animated)


def finish():
    global gamelose
    gamelose=True

pgzrun.go()