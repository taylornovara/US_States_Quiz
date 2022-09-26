"""
A small quiz program that uses Turtle Graphics to display that names of US states to a blank US Map.
"""
import turtle

# Constant that stores the image file of our map
IMAGE = "blank_states_img.gif"

# Creates the screen and adds the blank US Map as the background to use for our quiz
screen = turtle.Screen()
screen.title("U.S. States Quiz")
screen.addshape(IMAGE)
turtle.shape(IMAGE)


# Screen only exits on click
screen.exitonclick()
