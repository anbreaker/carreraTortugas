import turtle
import random

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
    __colorTurtleSpanish = ('Roja', 'Naranja', 'Verde', 'Azul')
    
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


    def competir(self):

      hayGanador = False                                    #flag
      while not hayGanador:
        for tortuga in self.corredores:
          avance = random.randint(1,6)
          tortuga.forward(avance)

          if tortuga.position()[0] >= self.__finishLine:
             hayGanador = True
             print("La tortuga de color {} ha ganado".format(tortuga.color()[0])) #tortuga.color()[0] Guetter de color de turtle
             break                                           #Una vez llega una tortuga paramos el bucle


if __name__ == '__main__':
    circuito = Circuito(340,180)
    circuito.competir()
