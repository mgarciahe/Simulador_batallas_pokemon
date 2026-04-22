#Se crea la base plantilla general. esta debe ser abstracta ya que debe heredar a sus hijos.
from abc import ABC, abstractmethod


class Pokemon(ABC):

    #Creamos el constructor con sus atributos 

    def __init__(self, nombre, hp_maximo, energia_maxima):

        self.nombre = nombre
        self.hp_maximo = hp_maximo
        self.energia_maxima = energia_maxima

        #Atributos Privados, no los podemos modificar desde afuera

        self.__hp_actual = hp_maximo
        self.__energia_actual = energia_maxima

        #atributo para todas las clases, actuara como escudo para el siguiente ataque, lo cambiamos a True en el metodo defender
        self.defendiendo = False

    @property
    def hp_actual(self):
        return self.__hp_actual


    @hp_actual.setter
    def hp_actual(self, valor):

        if valor < 0:
            self.__hp_actual = 0
        elif valor > self.hp_maximo:
            self.__hp_actual = self.hp_maximo
        else:
            self.__hp_actual = valor

    def mostrar_hp(self):
      print(f"HP Actual:  {self.hp_actual}")

    @property
    def energia_actual(self):
        return self.__energia_actual


    @energia_actual.setter
    def energia_actual(self, valor):

        if valor < 0:
            self.__energia_actual = 0
        elif valor > self.energia_maxima:
            self.__energia_actual = self.energia_maxima
        else:
            self.__energia_actual = valor

    #Seguimos creando los metodos que heredaran todas las clases hijas
    
    #Mostramos los datos del pokemon.
    def mostrar_estado(self):
        print(f"{self.nombre} [HP: {self.hp_actual}/{self.hp_maximo}] | [EP: {self.energia_actual}/{self.energia_maxima}]")

    #Metodo para defender consume 5 de energia
    def defender(self):
        if self.energia_actual >= 5
            self.energia_actual -= 5 
            self.defendiendo = True
            print (f"{self.nombre} esta en modo defensa")

    #Metodo descansar aumenta la energia en un 20
    def descansar(self):
        self.energia_actual += 20 
        print(f"{self.nombre} a recuperado 20 puntos de energia")
    
    #Creamos el metodo Abstracto Atacar, todos los hijos lo heredan pero lo usan diferente lo dejamos en pass
    def atacar(self, oponente):
        pass


