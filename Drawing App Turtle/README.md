# Simple Drawing App

A simple drawing application built using Python's turtle graphics library. Users can control a turtle-shaped pen to draw on the screen using keyboard commands.

## Features

- Move the pen forward and backward
- Turn the pen left and right
- Clear the drawing on the screen
- Responsive to keyboard input

## Requirements

- Python 3.12.4 or higher
- Turtle graphics library (included in Python's standard library)

## Usage

1. Run the `simple_drawing_app.py` script.
2. A window will open with a turtle-shaped pen in the center.
3. Use the following keyboard commands to control the pen:
   - `w`: Move the pen forward
   - `s`: Move the pen backward
   - `a`: Turn the pen left
   - `d`: Turn the pen right
   - `c`: Clear the drawing on the screen
4. Click on the window to give it focus so that it can respond to keyboard input.
5. Draw by moving the pen around using the keyboard commands.
6. To exit the application, close the window.

## Code Structure

The code is organized as follows:

1. Import the `turtle` module for drawing.
2. Set up the screen for drawing.
3. Create a turtle object (pen) that will be used for drawing.
4. Define functions for moving the pen forward, backward, turning left, turning right, and clearing the screen.
5. Set up key listeners for controlling the turtle's movements using the defined functions.
6. Keep the window open and responsive to user input using `screen.mainloop()`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.
