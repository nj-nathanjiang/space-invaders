import turtle as t


class ListOfBullets:

    def __init__(self):
        self.list_of_bullets = []

    def create_bullet(self, x):
        bullet = Bullet(x)
        self.list_of_bullets.append(bullet)


class Bullet(t.Turtle):

    def __init__(self, x_coor):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=1.75, stretch_len=0.25)
        self.penup()
        self.goto(x=x_coor, y=-300)
        self.color("white")
        self.y_move = 20

    def move(self):
        self.goto(x=self.xcor(), y=self.ycor() + self.y_move)

    def destroy(self):
        self.color("black")
