# Pong in Python 3
# Author: nscklye
# Start Date: 10/30/2022
# Last Update: 10/30/2022

import turtle

# Developing the Game Window
wn = turtle.Screen()
wn.title('Pong by nscklye')
wn.bgcolor('black')
wn.setup(height = 720, width = 1280)
wn.tracer(0)

# A - Left Paddle
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.color('white')
pad_a.penup()
pad_a.goto(-600, 0)
pad_a.shapesize(stretch_wid=5, stretch_len=1)

# B - Right Paddle
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape('square')
pad_b.color('white')
pad_b.penup()
pad_b.goto(600, 0)
pad_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.goto(0,0)
ball.penup()
ball.dx = 2
ball.dy = 2

# Functions
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

# Key bindings
wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

# Game Loop
while True:
    wn.update()
