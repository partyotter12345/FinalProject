#game

from graphics import *
import random,sched,time


#define window parameters
win = GraphWin('The Game', 1000,600)
win.yUp()
points = int(0)

def begingame():
    pass

def background():
    #define background
    lvl1 = Image(Point(500,300),"forestback.gif")
    lvl1.draw(win)

    


def enemies():

    #random enemy spawns, stays on screen for 0.5 secs

    for enemyspawn in list(range(10)):
        x=random.randint(50,950)
        y=random.randint(50,550)
        enemies=(x,y)
        enemy1 = Image(Point(x,y),"pikasmall.gif")
        enemy1.draw(win)
        time.sleep(1)
        enemy1.undraw()
        time.sleep(1)
    

def nearenemy():

    while points <= 6 :
        cx = enemy1(x)
        cy = enemy1(y)
        ux = p.getX()
        uy = p.getY()
        if abs(cx-ux)<=50 and abs(cy-uy)<=50:
            points = points +1
            return (True)
        return (points)
    


def hitmarker():
    
    while points <= 6 :
        p=win.getMouse()
        status, p=nearenemy()
        if status:
            hitmarker = Circle(Point(p(x),p(y)), 50)
            hitmarker.setFill("red")
            hitmarker.draw(win)

def pointcounter():
    global points
    return points >= 6


def main():
    global points
    
    background()
    enemies()
    hitmarker()
    nearenemy()
    
    
    
main()
