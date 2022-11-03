
#game

from graphics import *
import random,sched,time


#define window parameters
win = GraphWin('The Game', 1000,600)
win.yUp()

global pointvalue
pointvalue = 0

def begingame():
    pass

def background():
    #define background
    lvl1 = Image(Point(500,300),"forestback.gif")
    lvl1.draw(win)

    
def nearenemy(x,y,pointvalue):

    clickpoint=win.checkMouse()
    

    if clickpoint != None:
        cx = x
        cy = y
        ux = clickpoint.getX()
        uy = clickpoint.getY()
    
        if abs(cx-ux)<=50 and abs(cy-uy)<=50:

            pointvalue +=1
            hitmarker = Circle(Point(x,y), 100)
            hitmarker.setWidth(4)
            hitmarker.setOutline('red')
            hitmarker.draw(win)
            time.sleep(0.2)
            hitmarker.undraw()
            
            pointcounter = Text(Point(20, 20),pointvalue)
            pointcounter.setSize(18)
            pointcounter.draw(win)
            
            
        else:

            pointvalue +=0
            pointcounter = Text(Point(20, 20),pointvalue)
            pointcounter.setSize(18)
            pointcounter.draw(win)

            
            
            
            
            
            
   

        


    

def enemies(x,y):

    #random enemy spawns, stays on screen for 1 secs

    pass
        




#def points():
   # pointvalue = pointvalue + 1
    



    






def main():

    background()
    
    pointcounter = Text(Point(20, 20),pointvalue)
    pointcounter.setSize(18)
    pointcounter.draw(win)

    
    
    
    for enemyspawn in list(range(10)):
        

        x=random.randint(50,950)
        y=random.randint(50,550)
        enemy1 = Image(Point(x,y),"pikasmall.gif")
        enemy1.draw(win)
        time.sleep(1)
        nearenemy(x,y,pointvalue)
        enemy1.undraw()
        time.sleep(1)
        pointcounter.undraw()

    win.promptClose(win.getWidth()/2, 20)
        
    
    
    
main()
