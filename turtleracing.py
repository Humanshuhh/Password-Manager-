import turtle
import random
import time

WIDTH ,HEIGHT = 500 ,500

# screen setup
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title("Turtle racing")
screen.bgcolor("white")

# Race Settings
COLORS = ["Red","Blue","Orange","purple"]
NAMES =  ["Red","Blue","Orange","purple"]
NUM_TURTLES = 4
FINISH_LINE = 150
START_POSITION = -240
LANE_SPACING  = 50
FIRST_LANE_Y = 100

#DRAW TRACK
def track():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup

#Finish Line
    pen.goto(FINISH_LINE,200)
    pen.pendown()
    pen.pensize(4)
    pen.color("balck")
    pen.goto(FINISH_LINE,-200)
    pen.penup

  # FINISH LABEL
    pen.goto(FINISH_LINE + 10,200)
    pen.color("balck")
    pen.write("FINISH" ,font=("Arial", 14, "bold"))
    

 # START LINE
    pen.goto(START_POSITION,200)
    pen.down()
    pen.size(4)
    pen.color("gray")
    pen.goto(START_POSITION,-200)
    pen.penup()
#lane lines

    pen.pensize(1)
    pen.color("white")
    for i in range(NUM_TURTLES + 1):
        y = FIRST_LANE_Y + 40 - i * LANE_SPACING
        pen.goto(START_POSITION, y)
        pen.pendown()
        pen.goto(FINISH_LINE, y)
        pen.penup()

 # Title
    pen.goto(0, 260)
    pen.color("darkgreen")
    pen.write("🐢 TURTLE RACE 🐢", align="center", font=("Arial", 22, "bold"))


track()

time.sleep(10)