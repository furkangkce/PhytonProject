## ekranda rastgele yerlerde kaplumbağa simgelerinin çıkması turtle.teleport
## kaplumbağa lara basınca score artması turtle.onclik
## sayaç olucak bitince game over yazıcak turtle.ontimer
import time
import turtle
import random

from PIL.ImageChops import screen

##COUNDER


# Make a Backround for counder(sayaç)

game_board=turtle.Screen()
screen=turtle.Screen()
game_board.bgcolor("light blue")
game_board.title("Catch the Turtle")

gkce_turtle=turtle.Turtle()
gkce_turtle.penup()
gkce_turtle.hideturtle()
gkce_turtle.goto(0, 250)
gkce_turtle.color("black")
Score=0
gkce_turtle.write(f"Score: {Score}", align="center", font=("Arial", 20, "bold"))



gkce_turtle2=turtle.Turtle()
gkce_turtle2.hideturtle()
gkce_turtle2.penup()
gkce_turtle2.goto(0,280)
gkce_turtle2.color("Dark blue")

Remaningtime=20
def counder():
    global Remaningtime

    if Remaningtime>0:
        Remaningtime-=1
        screen.ontimer(counder,1000)
        gkce_turtle2.clear()
        gkce_turtle2.write(f"Remaning Time! : {Remaningtime}", align="center", font=("Arial", 20, "bold"))
    else:
            gkce_turtle2.color("red")
            gkce_turtle2.clear()
            gkce_turtle2.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

## rastgele yerde turtle oluşturma

gkce_turtle3=turtle.Turtle()
gkce_turtle3.color("dark green")
gkce_turtle3.shape("turtle")
gkce_turtle3.penup()
turtletime=20

def rastgele():
    global turtletime
    if turtletime > 0:
        turtletime -= 1
        screen.ontimer(rastgele,1000)
        gkce_turtle3.clear()
    x=random.randint(-230,230)
    y=random.randint(-230,230)
    gkce_turtle3.teleport(x,y)



# score up
def scoreup():
    global Score
    if Remaningtime>0:
        Score += 1
        gkce_turtle.clear()
        gkce_turtle.write(f"Score: {Score}", align="center", font=("Arial", 20, "bold"))
        gkce_turtle = turtle.onclick(rastgele)


rastgele()
counder()
turtle.done()









