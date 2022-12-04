from puntoc import puntoC
from matplotlib import pyplot as plt


def plot(x, y,x1,y1):
    ax = plt.axes()
    ax.arrow(x,y, x1,y1 , head_width=0.5, head_length=0.5)    
    return ax

class punto(puntoC):
    
    def cuadrante(self):
        if(self.x>=0 and self.y>=0):
            print("Cuadrante 1")
        elif (self.x<0 and self.y>=0):
            print("Cuadrante 2")
        elif self.x<0 and self.y<0:
            print("Cuadrante 3")
        else:
            print("Cuadrante 4")

    def vector(self,x1,y1):
        return plot(self.x,self.y,x1,y1)











 
