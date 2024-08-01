from p5 import *

def setup():
    size(640, 480)  # Set the window size to 640x480 pixels
    title("Hello World with p5py")  # Set the window title

def draw():
    background(255)  # Set the background color to white
    fill(0, 102, 153)  # Set the fill color for shapes and text
    text("Hello, World!", (10, 50))  # Draw the text "Hello, World!" at position (10, 50)
    
    # Draw a circle at the center of the canvas
    fill(255, 0, 0)  # Set the fill color for the circle to red
    ellipse((width / 2, height / 2), 100, 100)  # Draw a circle at the center with a diameter of 100 pixels

    # Draw a rectangle
    fill(0, 255, 0)  # Set the fill color for the rectangle to green
    rect((50, 200), 150, 100)  # Draw a rectangle at position (50, 200) with width 150 and height 100

run()