import turtle
import time
import random
delay = 0.1

#setting up the screen
win = turtle.Screen()
win.title('Snake Game')
win.bgcolor('black')
win.setup(width=600,height=600)
win.tracer(0)

#setup the snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.shapesize(0.5,0.5)
food.goto(50,50)

#function to move snake
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction  == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

#movement logic
def go_up():
    if head.direction is not 'down':
        head.direction = 'up'
def go_down():
    if head.direction is not 'up':
        head.direction = 'down'
def go_right():
    if head.direction is not 'left':
        head.direction = 'right'
def go_left():
    if head.direction is not 'right':
        head.direction = 'left'

#keyboard bindings
win.listen()
win.onkeypress(go_up,'w')
win.onkeypress(go_down,'s')
win.onkeypress(go_right,'d')
win.onkeypress(go_left,'a')


#main game loop 
while True:
    win.update()
    move()
    time.sleep(delay)


