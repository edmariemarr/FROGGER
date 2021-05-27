from graphics import *

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

    def collision(self, other):     # if frog and car collide
        if self.x < other.x + other.getWidth() and self.x + self.getWidth() > other.x and \
                self.y < other.y + other.getHeight() and self.y + self.getHeight() > other.y:
            return True
        return False

    def reset(self):    # if collision happens, bring frog back to square one
        self.undraw()
        self.frog = Image(Point(6.5, 2.5), "/img/froggy.png")

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
        if self.speed < -400:
            self.speed = 400
        if self.speed > 400:
            self.speed = -400

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

    def direction(self):
        if self.speed < 0:
            return "left"
        elif self.speed > 0:
            return "right"

def main():
    WIDTH = 600
    HEIGHT = 600
    win = GraphWin("FROGGER", WIDTH, HEIGHT)  # sets window
    win.setBackground("black")
    win.setCoords(0, 0, 13, 13)

    #   CARS
    myCars = [Car(6.5, 7, "/img/car.png", -2, win),
              Car(10.5, 7, "/img/car.png", -2, win),
              Car(3.5, 9, "/img/racing.png", 3, win),
              Car(8.5, 9, "/img/racing.png", 3, win),
              Car(2.5, 5, "/img/racing.png", 3, win),
              Car(12.5, 5, "/img/racing.png", 3, win)]

    gameOver = False
    x_frog = 6.5
    y_frog = 2.5

    #   FROG
    froggerPlayer = Frog(x_frog, y_frog, win)
    froggerPlayer.create(win)

    while not gameOver:
        key = win.checkKey()
        if key:  # FROG MOVEMENT WITH WASD KEYS
            froggerPlayer.undraw()
            if key == 'w':
                y_frog += 1.9
                froggerPlayer.frog.move(0, y_frog)
            elif key == 'a':
                x_frog -= 1.9
                froggerPlayer.frog.move(x_frog, 0)
            elif key == 's':
                y_frog -= 1.9
                froggerPlayer.frog.move(0, y_frog)
            elif key == 'd':
                x_frog += 1.9
                froggerPlayer.frog.move(x_frog, 0)
            froggerPlayer = Frog(x_frog, y_frog, win)
            froggerPlayer.create(win)

        #   CARS MOVEMENT
        #   NEED TO WORK ON CAR TRAFFIC WITH BOUNDS
        for cars in myCars:
            cars.movecars()
            time.sleep(0.4)

        #   CALCULATE COLLISION
        #   NEED TO WORK ON COLLISION BRINGING THE FROG TO SQUARE ONE
        if froggerPlayer.collision(cars):
            froggerPlayer.reset()
            froggerPlayer.create(win)

        #   GAME OVER IF FROG LIVES REACH 0
        if froggerPlayer.lives == 0:
            gameOver = True

        #   FROG REACHES HOME
        #   NEED TO WORK ON TEXT APPEARANCE
        if froggerPlayer.getHeight() >= win.getHeight():
            time.sleep(5)
            gameOver = True

    if gameOver:  # CLOSE GAME
        win.close()


main()
