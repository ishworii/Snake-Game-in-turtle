import turtle
import time
import random

delay = 0.1
segments = []
score = 0
high_score = 0

#setting up the screen
win = turtle.Screen()
win.title('Snake Game')
win.bgcolor('black')
win.setup(width=600,height=600)
win.tracer(0)

#setup the snake head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('blue')
head.penup()
head.goto(0,0)
head.direction = 'stop'

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.penup()
food.goto(50,50)

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score:0 High Score:0',align='center',font=('Courier',24,'normal'))


#add a segment
def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape('circle')
    new_segment.color('gray')
    new_segment.penup()
    segments.append(new_segment)

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

def snake_dies():
    win.bgcolor('red')
    head.goto(0,0)
    head.direction = 'stop'

    #hide the segments
    for segment in segments:
        segment.goto(1000,1000)

    #clear the segments
    segments.clear()

    #reset the score
    score = 0
        
    #reset the delay
    delay = 0.1

    #update the score display
    pen.clear()
    pen.write(f'Score: {score} High Score: {high_score}',align='center',font=('Courier',24,'normal'))
    time.sleep(2)
    win.bgcolor('black')


#keyboard bindings
win.listen()
win.onkeypress(go_up,'w')
win.onkeypress(go_down,'s')
win.onkeypress(go_right,'d')
win.onkeypress(go_left,'a')


#main game loop 
while True:
    win.update()
    time.sleep(delay)
    #collision with boundary
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        snake_dies()

    #snake eats food
    if head.distance(food) < 15 :
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        
        add_segment()
        
        #Shorten the delay
        #delay -= 0.001

        #increase the score
        score += 10
        
        if score > high_score : 
            high_score = score
        pen.clear()
        pen.write(f'Score:{score} High Score:{high_score}',align='center',font=('Courier',24,'normal'))

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    
    #check for head collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            snake_dies()
    time.sleep(delay)

win.mainloop()
