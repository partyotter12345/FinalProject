from graphics import *


def begingame():

    startScreen = Rectangle(Point(0,0), Point(1000,600))
    startScreen.setFill('green')
    startScreen.draw(win)

    startMessage1 = Text(Point(500,450), 'A group of invaders are trying to steal your gold!')
    startMessage2 = Text(Point(500,375), 'To capture them you must click on them before they disappear')
    startMessage3 = Text(Point(500,300), 'To advance to the next level, you must capture at least 8 invaders')
    startMessage4 = Text(Point(500,100), 'Game will begin in 10 seconds...')

    startMessage1.setTextColor('black')
    startMessage2.setTextColor('black')
    startMessage3.setTextColor('black')
    startMessage4.setTextColor('black')

    startMessage1.setSize(22)
    startMessage2.setSize(22)
    startMessage3.setSize(22)
    startMessage4.setSize(22)

    startMessage1.setStyle('bold')
    startMessage2.setStyle('bold')
    startMessage3.setStyle('bold')
    startMessage4.setStyle('bold')

    startMessage1.draw(win)
    startMessage2.draw(win)
    startMessage3.draw(win)
    startMessage4.draw(win)

    time.sleep(2) #change this back to 10 after work
    
    startScreen.undraw()
    startMessage1.undraw()
    startMessage2.undraw()
    startMessage3.undraw()
    startMessage4.undraw()
