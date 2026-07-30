import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    try:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt = "Guess an state").title()
    except:
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        writer = turtle.Turtle()
        writer.penup()
        state_data = data[data["state"]== answer_state]
        writer.goto(state_data["x"].item(),state_data["y"].item())
        writer.write(answer_state)


#pandas import
data[~data["state"].isin(guessed_states)].to_csv("states_to_learn.csv", index=False)
pd.Series(guessed_states, name = "Guessed States").to_csv("guessed_states.csv", index = False)