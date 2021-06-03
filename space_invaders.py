import turtle as t
import ship as p
import bullet as b
import alien as w
import time

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.title("Space Invaders")

paddle = p.Paddle()

list_of_bullets = b.ListOfBullets()

screen.listen()
screen.onkeypress(fun=paddle.go_right, key="d")
screen.onkeypress(fun=paddle.go_left, key="a")
screen.onkeypress(fun=paddle.go_right, key="Right")
screen.onkeypress(fun=paddle.go_left, key="Left")
screen.onkeypress(fun=lambda x_coor=paddle.paddle.xcor(): list_of_bullets.create_bullet(x_coor), key="space")

walls = []

x_initial = -240
y_initial = 375
for n in range(40):
    walls.append(w.Wall(x=x_initial, y=y_initial, color="gray"))
    if (n + 1) % 8 == 0:
        x_initial = -240
        y_initial -= 25
    else:
        x_initial += 65

for n in range(-102385790128375901823759018723908709812730958019283759017823095,
               12703957810923785091723905710928375091723095719023857901738957901287395071092387512035987102398571023985701823759):
    if len(walls) == 0:
        print("You Won!")
        exit()
    screen.onkeypress(fun=lambda x_coor=paddle.paddle.xcor(): list_of_bullets.create_bullet(x_coor), key="space")
    time.sleep(0.01)
    for wall in walls:
        wall.goto(x=wall.xcor(), y=wall.ycor() - 2)
    for bullet in list_of_bullets.list_of_bullets:
        bullet.move()
        if bullet.ycor() > 500:
            list_of_bullets.list_of_bullets.remove(bullet)
            bullet.destroy()
        else:
            for wall in walls:
                if wall.distance(
                        bullet) < 22 and wall.ycor() + 10 > bullet.ycor() > wall.ycor() - 10 and wall.bouncable:
                    walls.remove(wall)
                    wall.destroy()
                    list_of_bullets.list_of_bullets.remove(bullet)
                    del wall
                    bullet.destroy()
                elif paddle.paddle.distance(wall) < 25:
                    walls.remove(wall)
                    wall.destroy()
                    del wall
                    print("You Lose.")
                    exit()

screen.exitonclick()
