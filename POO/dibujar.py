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
    return t.mainloop()

