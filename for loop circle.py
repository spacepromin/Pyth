import turtle

wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("alex & tess")

tess=turtle.Turtle()
tess.color("blue")
tess.pensize(6)

for i in[0,1,2,3,4,5,6,7,8,9,10,11]:
    tess.forward(90)
    tess.left(30)

alex=turtle.Turtle()
alex.color("green")
alex.pensize(5)

for i in range(12):
    alex.forward(80)
    alex.left(30)

maya=turtle.Turtle()
maya.color("yellow")
maya.pensize(5)

for i in range(12):
    maya.forward(70)
    maya.left(30)


blen=turtle.Turtle()
blen.color("red")
blen.pensize(5)

for i in range(12):
    blen.forward(60)
    blen.left(30)

b1=turtle.Turtle()
b1.color("blue")
b1.pensize(5)

for i in range(12):
    b1.forward(50)
    b1.left(30)

b2=turtle.Turtle()
b2.color("green")
b2.pensize(5)

for i in range(12):
    b2.forward(40)
    b2.left(30)

b3=turtle.Turtle()
b3.color("yellow")
b3.pensize(5)

for i in range(12):
    b3.forward(30)
    b3.left(30)

b4=turtle.Turtle()
b4.color("red")
b4.pensize(6)

for i in range(12):
    b4.forward(20)
    b4.left(30)

b5=turtle.Turtle()
b5.color("darkblue")
b5.pensize(6)

for i in range(12):
    b5.forward(10)
    b5.left(30)

b6=turtle.Turtle()
b6.color("black")
b6.pensize(7)

for i in range(12):
    b6.forward(5)
    b6.left(30)
wn.mainloop()