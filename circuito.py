import turtle

#Objeto

#-------------------#
#      Circuito     #
#-------------------#
#  - corredores()   #
#  - pantalla       #
#-------------------#
#  - competir()     #
#  - get y set      #
#-------------------#

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'orange', 'green', 'blue')
    
    def __init__(self, width, height):
      self.width = width
      self.height = height

      self.__screen = turtle.Screen()                       #Metodo de pantalla de turtle
      self.__screen.setup(width, height)                    #Definimos tamaño
      self.__screen.bgcolor('lightgray')                    #Definimos el color de la pantalla
      self.__startLine = -width / 2 + 20                    #Iniciamos la posicion de salidas para nuestra pantalla
      self.__finishLine = width /2 - 20

      self.__createRunners()

    def __createRunners(self):                              #Constructor de corredores
        for i in range(4):
          new_turtle = turtle.Turtle()                      #creacion de tortugas
          new_turtle.shape('turtle')                        #Forma a las tortugas
          new_turtle.penup()                                #Metodo que no pinta las lineas
          new_turtle.color(self.__colorTurtle[i])           #Metodo para cambiar el color de los corredores
          new_turtle.setposition(self.__startLine, self.__posStartY[i])  #Definimos la colocacion de cada tortuga segun su posicion
          self.corredores.append(new_turtle)                #Agregamos a la lista de corredores






if __name__ == '__main__':
    circuito = Circuito(540,380)
