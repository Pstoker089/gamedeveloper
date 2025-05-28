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
    global j
    numbgaps=len(itemstolayout)+1
    gapsize=WIDTH/numbgaps
    random.shuffle(itemstolayout)
    for i,j in enumerate(itemstolayout,1):
        newx=i*gapsize
        j.x=newx

        
    

def animateitems(itemstoanimate):
    for i in itemstoanimate:
        duration=startspeed-currentlevel
        i.anchor=("center","bottom")
        animated=animate(i,duration=duration,on_finished=finish,y=HEIGHT)
        animations.append(animated)

def on_mouse_down(pos):
    for i in everything:
        if i.collidepoint(pos):
            if "paper" in i.image:
               nextstage()
            else:
               finish()

def stopanimations(ats):
    for i in ats:
        if i.running:
            i.stop()

def nextstage():
    global gamewin
    global currentlevel
    global totallevel
    global animations
    global everything
    stopanimations(animations)
    if currentlevel==totallevel:
        gamewin=True
    else:
        currentlevel+=1
        everything=[]
        animations=[]



def finish():
    global gamelose
    gamelose=True

pgzrun.go()