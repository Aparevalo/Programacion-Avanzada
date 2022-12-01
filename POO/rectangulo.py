import turtle
def dibujar_puntos(l,w):  
    t = turtle.Turtle()
    t.forward(l*20) 
    t.left(90) 
    t.forward(w*20) 
    t.left(90) 
    t.forward(l*20) 
    t.left(90) 
    t.forward(w*20) 
    t.left(90)
    return t
class rectangulo:

    x=0
    y=0

    def ing(self,x,y):
        self.x=x
        self.y=y

    def dibujar(self,x1,y1):
            px=(x1-self.x)
            py=(y1-self.y)
            dibujar_puntos(px,py)

