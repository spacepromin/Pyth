import turtle

def dreaw(t, sz):
    for i in ["green","yellow","red","blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn=turtle.Screen()
wn.bgcolor("black")
alex=turtle.Turtle()
alex.pensize(4)

size=20

for i in range(18):
    dreaw(alex,size)
    size=size+10
    alex.forward(10)
    alex.right(18)


wn.mainloop()
