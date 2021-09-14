import turtle

turtle.shape('turtle')
turtle.stamp()

def up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def escape():
    turtle.reset()
    turtle.stamp()
    

turtle.onkeypress(up,'w')
turtle.onkeypress(right,'d')
turtle.onkeypress(left,'a')
turtle.onkeypress(down,'s')
turtle.onkeypress(escape,'Escape')
turtle.listen()
turtle.exitonclick()
