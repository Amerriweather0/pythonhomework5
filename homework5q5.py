from graphics import *


def logistic(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
    return x


def main():
    # Create the graphics window
    win = GraphWin("Logistic Function", 600, 400)

    # Draw x-axis
    x_axis = Line(Point(50, 350), Point(550, 350))
    x_axis.draw(win)

    # Draw y-axis
    y_axis = Line(Point(50, 350), Point(50, 50))
    y_axis.draw(win)

    # Starting values
    k = 3.9
    x = 0.5

    # Plot 100 points
    for n in range(100):
        y = logistic(k, x, 1)

        # Convert values to screen coordinates
        screen_x = 50 + n * 5
        screen_y = 350 - y * 300

        point = Point(screen_x, screen_y)
        point.draw(win)

        # Use the current output as the next input
        x = y

    # Wait for a mouse click before closing
    win.getMouse()
    win.close()


main()