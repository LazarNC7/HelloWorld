from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race?")
colors=["red", "orange", "yellow", "green", "blue", "purple"]
if user_bet:
    is_race_on=True

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230,y=-100)
# print(user_bet)

t = []

for index in range(6):
    t.append(Turtle("turtle"))
    t[index].color(colors[index])
    t[index].penup()
    t[index].goto(x=-230,y=-100 + 45 * index)

while is_race_on:
    for turt in t:
        if turt.xcor() > 230:
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"You ve won. The {winning_color} turtle is the answer")
            else:
                print(f"You ve lost. The {winning_color} turtle is the answer")

            is_race_on = False
        rand_distance = random.randint(0,10)
        turt.forward(rand_distance)

    

screen.exitonclick()