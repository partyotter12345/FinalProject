from graphics import *
import random,sched,time
win = GraphWin('The Game', 1000,600)
win.yUp()

def background():
    # Draw the sky
    sky = Rectangle(Point(0,0), Point(win.getWidth(), win.getHeight()))
    sky.setFill("sky blue")
    sky.draw(win)

    # Draw the dirt
    dirt = Rectangle(Point(0,0), Point(1000, 90))
    dirt.setFill("sienna")
    dirt.draw(win)

    
    # Draw the grass
    grass = Rectangle(Point(0,90), Point(1000,110))
    grass.setFill("sea green")
    grass.draw(win)

    grasspetal1 = Text(Point(500,100), "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    grasspetal1.setSize(36)
    grasspetal1.setStyle("bold")
    grasspetal1.setTextColor("sea green")

    grasspetal2 = grasspetal1.clone()
    grasspetal2.move(15,0)
    
    grasspetal1.draw(win)
    grasspetal2.draw(win)

    # Draw the clouds


    #First Cloud
    cloudbot1 = Oval(Point(425,425), Point(575,475))
    cloudbot1.setFill("white")
    cloudbot1.setOutline("white")

    cloudtop1 = Circle(Point(475,475),25)
    cloudtop1.setFill("white")
    cloudtop1.setOutline("white")

    cloudtop2 = Circle(Point(525,475), 35)
    cloudtop2.setFill("white")
    cloudtop2.setOutline("white")

    cloudbot1.draw(win)
    cloudtop1.draw(win)
    cloudtop2.draw(win)

    #Second Cloud
    cloudbot2 = cloudbot1.clone()
    cloudtop3 = cloudtop1.clone()
    cloudtop4 = cloudtop2.clone()

    cloudbot2.move(-300,-100)
    cloudtop3.move(-300,-100)
    cloudtop4.move(-300,-100)

    cloudbot2.draw(win)
    cloudtop3.draw(win)
    cloudtop4.draw(win)

    #Third Cloud

    cloudbot3 = cloudbot1.clone()
    cloudtop5 = cloudtop1.clone()
    cloudtop6 = cloudtop2.clone()

    cloudbot3.move(250,-100)
    cloudtop5.move(250,-100)
    cloudtop6.move(250,-100)

    cloudbot3.draw(win)
    cloudtop5.draw(win)
    cloudtop6.draw(win)

    #Sun

    sun = Circle(Point(1000,600), 110)
    sun.setFill("orange")
    sun.setOutline("tomato")
    sun.draw(win)

    
        
                

    
    
    #mainbackground = Image(Point(500,300),"forestback.gif")
    #lvl1.draw(win)
    
def main():
    background()

main()
