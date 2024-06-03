import turtle
from random import randint

wn = turtle.Screen()
wn.title("Carrera de Tortugas")
wn.bgcolor("white")


turtle.penup()
turtle.goto(-140, 140)
for step in range(15):
    turtle.write(step, align='center')
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(150)
    turtle.penup()
    turtle.backward(160)
    turtle.left(90)
    turtle.forward(20)

turtles = [] 
colors = ["pink", "orange", "magenta", "red"]
for i in range(4):
    new_turtle = turtle.Turtle()
    new_turtle.color(colors[i])
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.goto(-160, 100 - i * 30)
    new_turtle.pendown()
    turtles.append(new_turtle)

winner = None
while not winner:
    for tortuga in turtles:
        tortuga.forward(randint(1, 5))
        if tortuga.xcor() >= 140: 
            winner = tortuga
            winner.right(720) 
wn.mainloop()
