"""
A small quiz program that uses Turtle Graphics to display that names of US states to a blank US Map.
"""
import turtle
import pandas as pd

# Constant that stores the image file of our map
IMAGE = "blank_states_img.gif"

# Creates the screen and adds the blank US Map as the background to use for our quiz
screen = turtle.Screen()
screen.title("U.S. States Quiz")
screen.addshape(IMAGE)
turtle.shape(IMAGE)


# Plots the coordinates on the map for each state
def get_mouse_click_coordinates(x_cor, y_cor):
    print(x_cor, y_cor)


# Listens for mouse click and calls our coordinates function
turtle.onscreenclick(get_mouse_click_coordinates)

is_game_on = True
while is_game_on:
    # Displays an input and asks the user to enter a state
    user_answer = turtle.textinput(title="U.S. States", prompt="Enter a State:").title()

    # Reads the states csv
    states_data = pd.read_csv("50_states.csv")
    # Checks user answer, if correct, writes it to blank map
    if states_data["state"].eq(user_answer).any():
        x = int(states_data[states_data.state == user_answer].x)
        y = int(states_data[states_data.state == user_answer].y)
        answer = turtle.Turtle()
        answer.hideturtle()
        answer.penup()
        answer.setposition(x, y)
        answer.write(user_answer)
    else:
        pass

# Keeps screen open
turtle.mainloop()
