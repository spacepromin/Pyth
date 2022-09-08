import turtle

wn=turtle.Screen()

wn.title("mintesnot")



alex=turtle.Turtle()

clrs = ["blue","green","yellow","red"]
for c in clrs:
    alex.color(c)
    alex.pensize(6)
    alex.backward(100)
    alex.left(90)


alex=turtle.Turtle()

clrs = ["blue","green","yellow","red"]
for g in clrs:
    alex.color(g)
    alex.pensize(6)
    alex.backward(-100)
    alex.left(90)

a1=turtle.Turtle()

clrs = ["blue","green","yellow","red"]
for k in clrs:
    a1.color(k)
    a1.pensize(6)
    a1.backward(-100)
    a1.left(-90)

a2=turtle.Turtle()

clrs = ["blue","green","yellow","red"]
for f in clrs:
    a2.color(f)
    a2.pensize(6)
    a2.forward(-100)
    a2.left(-90)

wn.mainloop()