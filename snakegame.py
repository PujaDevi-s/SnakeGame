#import
from turtle import Turtle, Screen
import time
import random

#Constants
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Screen Setup
screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#snake creation with 3 box
segments = []
for position in STARTING_POSITIONS:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


head=segments[0]

# Food Creation
food = Turtle()
food.shape("circle")
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.color("blue")
food.speed("fastest")

# Food in Random position (x,y) axis
random_x=random.randint(-280, 280)
random_y=random.randint(-280, 280)
food.goto(random_x, random_y)

#ScoreBoard Creation
scoreboard = Turtle()
score = 0
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(0,265)
scoreboard.hideturtle()
scoreboard.write(f"Score:{score}", align=ALIGNMENT, font=FONT)

#Screen listening to users action
screen.listen()

# up button to move in upwards direction
def up():
    if head.heading()!=DOWN: # snake facing up direction should not move in down direction
        head.setheading(UP)

# left button to move in left direction      
def left():
    if head.heading()!=RIGHT:     
        """ Snake facing in left direction can move up, down only.
        Right direction not allowed"""
        head.setheading(LEFT)

# Right button to move in right direction              
def right():
    if head.heading()!=LEFT:   #snake facing the right direction cannot move to left direction
        head.setheading(RIGHT)

# Down button to move in down direction      
def down():
    if head.heading()!=UP:     # snake facing the down direction cannot move to up direction
        head.setheading(DOWN)

# user controls for key press
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")

# game ends when game_is_on is False
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)         
    """ determines the speed of snake as 0.1 second it is fast, 
    to make it slow give 0.3 second inside the time.sleep()"""

    # changing the position of all the part of snake to 1 step forward except head
    for seg_num in range(len(segments)-1,0,-1):  # head is removed from the range, stop = 0 means 0 will not be executed
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)

    # moving the snake foward for 1 time during each iteration
    head.forward(MOVE_DISTANCE)

# Detect collision with food
    if head.distance(food) < 15:
        # moving the food to new location once the snake had collision with food
        number_x = random.randint(-280, 280)
        number_y = random.randint(-280, 280)
        food.goto(number_x, number_y)
        # Increase the snake length once it has eaten the food
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(segments[-1].position())
        segments.append(new_snake)
        # Adding a value 1 in score 
        score+=1
        # Making the updated scoreboard visible to users
        scoreboard.clear()
        scoreboard.write(f"Score: {score}", align=ALIGNMENT, font=FONT)


   
# Detect collision with wall
    
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or  head.ycor() < -280:
        # game over once the snake hits the wall
        game_is_on = False
        # creating a turtle to display a "Game Over" text at center of the screen
        gameovertext = Turtle()
        gameovertext.goto(0,0)
        gameovertext.color("white")
        gameovertext.write("GAME OVER", align=ALIGNMENT, font=FONT)

        
# Detect collision with tail
    for segment in segments[1:]: 
        if head.distance(segment) < 10:
              # game over once the snake bites its own tail
              game_is_on = False
              # creating a turtle to display a "Game Over" text at center of the screen
              gameovertext = Turtle()
              gameovertext.goto(0,0)
              gameovertext.color("white")
              gameovertext.write("GAME OVER", align=ALIGNMENT, font=FONT)


screen.exitonclick()
