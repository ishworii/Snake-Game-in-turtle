import turtle

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


#main game loop 
while True:
    win.update()
    move()
