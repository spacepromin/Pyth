import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("alex & tess")

tess=turtle.Turtle()
tess.color("hotpink")
tess.pensize(6)

alex=turtle.Turtle()

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(80)


alex.color("lightgreen")
alex.forward(70)
alex.left(90)
alex.color("green")
alex.pensize(6)
alex.forward(40)
alex.left(90)
alex.forward(70)
alex.left(90)

alex.right(180)
alex.forward(80)

wn.mainloop()

