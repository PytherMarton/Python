import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("red")
# wn.bgpic("space.jpg")
wn.title("Simple Python game by @Pyter")
# wn.tracer(1.5)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score 0", align ="center", font=("Courier", 24, "normal"))

score = 0

mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()


player = turtle.Turtle()
player.color("blue")
player.shape("arrow")
player.penup()
player.shapesize(stretch_wid=1, stretch_len=3)

goal = turtle.Turtle()
goal.color("white")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-300, 300), random.randint(-300, 300))

speed = 0

turtle.listen()

def turnleft():
    player.left(30)


def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    speed += -1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)

    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)


    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)

    if goal.xcor() > 290 or goal.xcor() < -290:
        goal.right(180)
    
    if goal.ycor() > 290 or goal.ycor() < -290:
        goal.right(180)

    if isCollision(player, goal):
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align ="center", font=("Courier", 24, "normal")) 
        goal.setposition(random.randint(-300, 300), random.randint(-300, 300))
        goal.right(random.randint(0,360))

    goal.forward(3)

delay = raw_input("Press Enter to finish.")