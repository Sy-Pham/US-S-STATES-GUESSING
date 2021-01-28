import turtle
import pandas as pd


# setup screen
screen = turtle.Screen()
screen.title("US's States Guessing")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# load data
data = pd.read_csv("50_states.csv")



# run game
num_states = 0
while num_states < 50:
    user_answer = screen.textinput(title=f"{num_states}/50 Correct States", prompt="what's a name of state")
    user_answer = user_answer.lower()

    
       

    state_data = data[data.state.str.lower() == user_answer]
    if len(state_data) > 0:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        num_states += 1


screen.exitonclick()
