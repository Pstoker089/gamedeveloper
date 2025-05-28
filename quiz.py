import pgzrun

TITLE="FUN QUIZ"
WIDTH=800
HEIGHT=800

scrollerbox=Rect(0,0,800,80)

def draw():
    screen.fill("black")
    screen.draw.filled_rect(scrollerbox,"dark green")

def update():
    pass

pgzrun.go()