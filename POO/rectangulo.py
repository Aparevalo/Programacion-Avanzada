import turtle
from puntoc import puntoC

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

class rectangulo(puntoC):

    x=0
    y=0
    
    def dibujar(self,x1,y1):
            px=(x1-self.x)
            py=(y1-self.y)
            dibujar_puntos(px,py)

    def base(self,x1,y1):
        base=y1-self.y
        print("Base: "+str(base))

    def altura(self,x1,y1):
        altura=x1-self.x
        print("Altura: "+str(altura))

    def area(self,x1,y1):
        base=y1-self.y
        altura=x1-self.x
        area=base*altura
        print("Area: "+str(area))