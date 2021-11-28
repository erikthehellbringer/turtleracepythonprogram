from turtle import Turtle, Screen
import random as rand
#this function creates all the turtles and puts'em into an array called all_turtles
def make_turtle(x,y):
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x, y)
        y += 40 #every turtle positions at new place. so plus the y coordinate
        all_turtles.append(new_turtle)


def race(user_bet):
    if user_bet:
        is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            #if the current turtle reaches beyond x coordinate 230. the turtle wins
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You won. {winning_color} is the victor.")
                else:
                    print(f"{winning_color} is the victor. you lost.")
            #the current turtle's random running distance
            random_distance = rand.randint(0, 10)
            turtle.forward(random_distance)


screen = Screen()
screen.setup(width = 500, height= 400)
user_bet=screen.textinput("Make your bet", "which turtle will win the race?")
colors =["red", 'yellow', 'blue','brown', 'pink', 'black']
all_turtles=[]
x =-240
y= -100
make_turtle(x,y)
race(user_bet)
screen.exitonclick()