from graphics import *
import math

class Frog:
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.win = win
        self.frog = Image(Point(self.x, self.y), "/img/froggy.png")  # sets image of frog
        self.lives = 3  # starting with 3 lives

    def create(self, win):  # create frog
        self.frog.draw(win)
        win.update()

    def undraw(self):  # undraw frog
        self.frog.undraw()

    def getWidth(self):  # gets width of frog
        return self.frog.getWidth()

    def getHeight(self):  # gets height of frog
        return self.frog.getHeight()

    def getX(self):  # receives x value
        return self.x

    def getY(self):  # receives y value
        return self.y

    def leftBound(self):  # calculates left bound
        left = (self.frog.getAnchor().getX() - self.frog.getWidth() / 2)
        return int(left)

    def rightBound(self):  # calculates right bound
        right = (self.frog.getAnchor().getX() + self.frog.getWidth() / 2)
        return int(right)

    def collision(self, other):     # if frog and car collide / or if frog and lilypad collide
        return (math.fabs(self.getX() - other.getX()) * 2) < (self.getWidth() + other.getWidth()) and \
                (math.fabs(self.getY() - other.getY()) * 2) < (self.getHeight() + other.getHeight())

    def reset(self, win):    # if collision happens, bring frog back to square one
        self.undraw()
        self.frog = Image(Point(6.5, 2.5), "/img/froggy.png")
        self.frog.draw(win)
        win.update()

class Car:
    def __init__(self, x, y, image, speed, win):
        self.x = x
        self.y = y
        self.speed = speed
        self.car = Image(Point(self.x, self.y), image)  # sets image of car
        self.car.draw(win)

    def movecars(self):  # moves cars
        self.x += self.speed
        self.car.move(self.speed, 0)

    def getWidth(self):  # gets width of car
        return self.car.getWidth()

    def getHeight(self):  # gets height of car
        return self.car.getHeight()

    def getX(self):  # receives x value
        return self.x

    def getY(self):  # receives y value
        return self.y

    def leftBound(self):  # calculates left bound
        left = self.car.getAnchor().getX() - self.car.getWidth() / 2
        return int(left)

    def rightBound(self):  # calculates right bound
        right = self.car.getAnchor().getX() + self.car.getWidth() / 2
        return int(right)

    def getDirection(self):
        if self.speed < 0:
            return "left"
        else:
            return "right"

class Home:
    def __init__(self, x, y, win):
        self.x = x
        self.y = y
        self.win = win
        self.pad = Image(Point(self.x, self.y), "/img/lilypad.png")     # sets image of lilypad
        self.pad.draw(win)

    def getWidth(self):  # gets width of lilypad
        return self.pad.getWidth()

    def getHeight(self):  # gets height of lilypad
        return self.pad.getHeight()

    def getX(self):  # receives x value
        return self.x

    def getY(self):  # receives y value
        return self.y

def main():
    WIDTH = 600
    HEIGHT = 600
    win = GraphWin("FROGGER", WIDTH, HEIGHT)  # sets window
    win.setBackground("black")
    win.setCoords(0, 0, 13, 13)
    homeline = Line(Point(0, 10), Point(13, 10))    # sets home line / where frog must go
    homeline.setFill("white")
    homeline.draw(win)
    baseline = Line(Point(0, 4), Point(13, 4))      # sets base line / where frog begins
    baseline.setFill("white")
    baseline.draw(win)

    # CREATE 3 LIVES
    life1 = Image(Point(1, 1), "/img/lives.png")
    life2 = Image(Point(1.5, 1), "/img/lives.png")
    life3 = Image(Point(2, 1), "/img/lives.png")
    life1.draw(win)
    life2.draw(win)
    life3.draw(win)

    # HOME
    pads = [Home(1.5, 11.5, win),
            Home(3.5, 11.5, win),
            Home(5.5, 11.5, win),
            Home(7.5, 11.5, win),
            Home(9.5, 11.5, win),
            Home(11.5, 11.5, win)]

    # CARS
    myCars = [Car(6.5, 7, "/img/car.png", -2, win),
              Car(10.5, 7, "/img/car.png", -2, win),
              Car(3.5, 9, "/img/racing.png", 3, win),
              Car(8.5, 9, "/img/racing.png", 4, win),
              Car(2.5, 5, "/img/racing.png", 2, win),
              Car(12.5, 5, "/img/racing.png", 3, win)]

    gameOver = False
    x_frog = 6.5    # starting x point for frog
    y_frog = 2.5    # starting y point for frog

    # FROG
    froggerPlayer = Frog(x_frog, y_frog, win)
    froggerPlayer.create(win)

    while not gameOver:
        key = win.checkKey()
        if key:  # FROG MOVEMENT WITH WASD KEYS
            froggerPlayer.undraw()
            if key == 'w':
                y_frog += 1
                froggerPlayer.frog.move(0, y_frog)
            elif key == 'a':
                x_frog -= 1
                froggerPlayer.frog.move(x_frog, 0)
            elif key == 's':
                y_frog -= 1
                froggerPlayer.frog.move(0, y_frog)
            elif key == 'd':
                x_frog += 1
                froggerPlayer.frog.move(x_frog, 0)
            froggerPlayer.create(win)

        # CARS MOVEMENT
        for cars in myCars:
            cars.movecars()
            time.sleep(0.5)

            if froggerPlayer.collision(cars):    # CAR COLLISION
                froggerPlayer.lives -= 1
                froggerPlayer.reset(win)
                break

        # LOSS OF LIVES AFTER COLLISION
        if froggerPlayer.lives == 2:
            life3.undraw()
        elif froggerPlayer.lives == 1:
            life2.undraw()
        elif froggerPlayer.lives == 0:
            life1.undraw()
            losing = Text(Point(6.5, 1.5), "FROGGER IS DEAD!")
            losing.setTextColor("red")
            losing.draw(win)
            gameOver = True

        # FROG REACHES HOME
        for lilypads in pads:
            if froggerPlayer.collision(lilypads):
                winning = Text(Point(6.5, 1.5), "FROGGER IS HOME SAFELY!")
                winning.setTextColor("white")
                winning.draw(win)
                gameOver = True
                break

    if gameOver:  # CLOSE GAME
        win.getMouse()
        win.close()

if __name__ == '__main__':
    main()