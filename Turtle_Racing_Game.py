import random,turtle
# Different race Turtles
shades=["blue","black","orange","green","yellow","violet","red"]
# Setting Background
turtle.bgcolor("skyblue")
turtle.write(font=("Arial",20,"bold"),arg="Turtle Race",align="center")
# Turtles traversing
l=turtle.Turtle("turtle")
l.color("red")
l.pensize(3)
l.penup()
l.setpos(-295,270)
l.pendown()
l.setpos(260,270)
l.ht()
# created racer class for making various racing turtles
class racer:
    def __init__(self,cl,x,y):
        self.colr=cl
        self.turt=turtle.Turtle("turtle")
        self.turt.color(cl)
        self.turt.pensize(5)
        self.turt.penup()
        self.turt.setpos(x,y)
        self.turt.setheading(90)
        self.turt.pendown()
# creating racer objects of various colors mentioned above
racers=[]
a=-250
for i in range(7):
    racers.append(racer(shades[i],a,-200))
    a=a+75
# main racing logic(Start,Stop,Winner) implemented
z=True
for k in range(200):
    for j in racers:
        if(j.turt.ycor()<255):
            j.turt.forward(random.randrange(5,10))
            if (j.turt.ycor()>=255):
                z=False
                print("Winner is",j.colr)
                break
    if(z==False):
        break
# making the turtle window steady
turtle.mainloop()
