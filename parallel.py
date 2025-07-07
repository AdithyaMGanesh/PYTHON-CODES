import turtle
def draw_parallelogram(color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)  
        turtle.left(60)
        turtle.forward(50)
        turtle.left(120)
    turtle.end_fill()

# Setup turtle
turtle.up()
turtle.goto(-50, -50)  
turtle.down()

draw_parallelogram("lightblue")

turtle.hideturtle()
turtle.done()
