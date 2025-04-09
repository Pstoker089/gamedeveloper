from turtle import Screen
import pgzrun ,random



WIDTH=500
HEIGHT=500
def draw():
    screen.draw.line((250,250),(250,0),"blue")
    screen.draw.text("Hello world", (250,250),fontname="opensans",fontsize=30,color="red",gcolor="white",owidth=1.5,ocolor="purple" )



    """size=25
    red=255
    blue=0
    screen.draw.circle((250,250),30,"red")
    for i in range(10):
        obj=Rect(250,250,size,size)
        obj.center=250,250
        screen.draw.filled_rect(obj,(red,0,blue))
        size+=25
        red-=20
        blue+=20"""

    

pgzrun.go()