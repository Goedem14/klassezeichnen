import turtle

class Zeichnen():
    def __init__(self,x_linie,y_linie):
        self.x_linie = x_linie
        self.y_linie = y_linie

    def linie_zeichnen (self,d):
        turtle.forward (d)

    def kreis_zeichnen(self,r):
        turtle.circle (r)
    
    def springe_zu(self,a,b): #hier muss ich nur selbst eine variable deklarieren 
        turtle.up()
        turtle.goto (a,b)
        turtle.down()


def main():
    turtle.speed(0)
    male = Zeichnen(100,100)
    male.linie_zeichnen(50)
    male.springe_zu(-100,-100)
    male.linie_zeichnen(50)
    male.springe_zu(50,30)
    
    for _ in range (1,100,2):
        turtle.color("green")
        turtle.begin_fill()
        male.kreis_zeichnen(10+_)
        turtle.end_fill()
    
    male.springe_zu(130,120)
    turtle.color("black")
    male.linie_zeichnen(120)

    turtle.exitonclick()


main () #so müssen die weiteren Programme immer aussehen 
