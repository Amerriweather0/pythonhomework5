from graphics import *
import math


def drawPolygon(win, n):
    center_x = 250
    center_y = 250
    radius = 150

    angle = 360 / n
    vertices = []

    for i in range(n):
        radians = math.radians(i * angle)

        x = center_x + radius * math.cos(radians)
        y = center_y + radius * math.sin(radians)

        vertices.append(Point(x, y))

    polygon = Polygon(vertices)
    return polygon


def graphPolygon(win, entry):
    # Get the number of sides from the Entry box
    n = int(entry.getText())

    # Create the polygon
    polygon = drawPolygon(win, n)

    # Draw the polygon
    polygon.draw(win)


def main():
    # Create the window
    win = GraphWin("Polygon", 500, 500)

    # Label
    label = Text(Point(150, 50), "Number of sides:")
    label.draw(win)

    # Entry box
    entry = Entry(Point(300, 50), 10)
    entry.draw(win)

    # Graph button
    button = Rectangle(Point(200, 90), Point(300, 130))
    button.draw(win)

    button_text = Text(Point(250, 110), "Graph")
    button_text.draw(win)

    # Wait for the first click
    click = win.getMouse()

    # Check whether the user clicked the Graph button
    if 200 <= click.getX() <= 300 and 90 <= click.getY() <= 130:
        graphPolygon(win, entry)

        # Change button text to Exit
        button_text.setText("Exit")

        # Wait for another click
        win.getMouse()

    # Close the window
    win.close()


main()