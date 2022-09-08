import turtle

wn=turtle.Screen()

back=input("enter_background_color")
wn.bgcolor(back)
wn.title("mintesnot, argaw")


alex=turtle.Turtle()
alex.color(input("enter color"))

alex.pensize(int(input("enter a number")))



alex.left(120)
alex.forward(150)
alex.left(120)
alex.forward(150)
alex.left(152)
alex.forward(190)
alex.left(148)
alex.forward(175)
alex.left(148)
alex.forward(190)
wn.mainloop()