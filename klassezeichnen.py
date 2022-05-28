import turtle

class Zeichnen():
    def __init__(self,x_linie,y_linie):
        self.x_linie = x_linie
        self.y_linie = y_linie

    def linie_zeichnen (self):
        turtle.forward (self.x_linie)

    def kreis_zeichnen(self,r):
        turtle.circle (r)
    
    def springe_zu(self,a,b): #hier muss ich nur selbst eine variable deklarieren 
        turtle.up()
        turtle.goto (a,b)
        turtle.down()


def main():
    male = Zeichnen(100,100)
    male.linie_zeichnen()
    male.springe_zu(-100,-100)
    male.linie_zeichnen()
    male.springe_zu(150,130)
    male.kreis_zeichnen(100)
    turtle.exitonclick()


main ()
