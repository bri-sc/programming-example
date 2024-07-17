import ipyturtle3 as turtle

def draw_sequence_with_turtle(sequence, unit=1, colour="aquamarine", canvas=(400, 400)):
    """
    This function can be used to plot a sequence using a turtle. After each value in the sequence the turtle will turn
    90 degrees.

    The canvas size is set to 400 x 400 pixels by default.

    Args:
        sequence : Sequence of number values
        colour: Colour of the background
        unit : Unit to travel on the canvas
        canvas: Two values for the x, y size of the plotting canvas.
        
    """

    # Print out the sequence values to plot
    print(f"Sequence values: {sequence}\n")

    # Create and display canvas with background colour
    myCanvas = turtle.Canvas(width=canvas[0],height=canvas[1])
    display(myCanvas)
    myTS = turtle.TurtleScreen(myCanvas)
    myTS.clear()
    myTS.bgcolor(colour)
    
    # Create turtle shape
    bob = turtle.Turtle(myTS)
    bob.shape("turtle")
    
    # Animate the sequence - repeats
    myTS.delay(50)  # Set the drawing delay in milliseconds
    for value in sequence:
        bob.forward(value * unit)  # Move the turtle forward
        bob.right(90)  # Turn the turtle 90 degrees