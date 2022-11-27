#from prueba1 import carro
from turtle import Turtle #importa todo el modulo

#print(prueba1.carro)
tortuga=Turtle()

class Coche:
    ruedas="si"
    def __init__(self,seats,color):
        print("nuevo coche creado")
        self.seats=seats
        self.color=color
        self.followers=0

coche=Coche(5,"rojo")

print(coche.color,coche.seats, coche.ruedas, coche.followers)