import turtle
pen =turtle.Pen()
pen.color('white','blue')
pen.speed(0)
pen.begin_fill()
for sq in range(72):
  for var in range(4):
    pen.forward(200)
    pen.left(90)
  pen.left(5)
pen.end_fill()
turtle.exitonclick()