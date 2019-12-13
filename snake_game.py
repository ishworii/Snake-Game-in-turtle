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
head.goto(0,100)
head.direction = 'stop'
