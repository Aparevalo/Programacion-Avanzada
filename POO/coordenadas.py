import turtle

def dibujar_puntos(l,w):  
    t = turtle.Turtle()
    t.forward(l*10) 
    t.left(90) 
    t.forward(w*10) 
    t.left(90) 
    t.forward(l*10) 
    t.left(90) 
    t.forward(w*10) 
    t.left(90)
    return t

class punto:
  
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def cuadrante(self):
        if(self.x>=0 and self.y>=0):
            print("Cuadrante 1")
        elif (self.x<0 and y>=0):
            print("Cuadrante 2")
        elif self.x<0 and y<0:
            print("Cuadrante 3")
        else:
            print("Cuadrante 4")

    def dibujar(self,x1,y1):
       
            px=(x1-self.x)
            py=(y1-self.y)
            dibujar_puntos(px,py)

       


    def vector(self,x1,y1):
        px=(x1-self.x)
        py=(y1-self.y)
        print("x =",px,"y =",py)


puntoA= punto(2,3)
puntoA.cuadrante()
puntoA.vector(7,8)
puntoA.dibujar(3,7)
turtle.mainloop()









 
