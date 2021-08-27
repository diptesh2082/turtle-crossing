from turtle import Turtle




STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.start()
    def move(self):
        self.fd(MOVE_DISTANCE)
    def start(self):
        self.goto(STARTING_POSITION)
    def finish(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

