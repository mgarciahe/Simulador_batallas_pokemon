#Se crea la base plantilla general

class Pokemon():

    #Creamos el constructor con sus atributos

    def __init__(self, nombre, hp_maximo, energia_maxima):

        #Creacion de atributos

        self.nombre = nombre

        self.hp_maximo = hp_maximo

        self.energia_maxima = energia_maxima


        #Atributos Privados

        self.__hp_actual = hp_maximo

        self.__energia_actual = energia_maxima
        

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

    
