import turtle

count = 4
while(count > 0):
    turtle.forward(500)
    turtle.left(90)
    count -= 1

count = 4
while(count > 0 ):
    turtle.forward(500-count*100)
    turtle.left(90)
    turtle.forward(500)
    turtle.penup()
    turtle.goto(0,0)
    count -= 1
    turtle.pendown()
    turtle.right(90)

count = 4
while(count > 0 ):
    turtle.goto(500,0)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(500-count*100)
    turtle.left(90)
    turtle.forward(500)
    turtle.penup()
    count -= 1
    turtle.right(180)
    
    
turtle.exitonclick()
