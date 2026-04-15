#Se crea la base plantilla general
class Pokemon():
    #Creamos el constructor con sus atributos
    def __init__(Self, nombre, hp_maximo, energia_maxima):
        #Creacion de atributos
        self.nombre = nombre
        self.hp_maximo = hp_maximo
        self.energia_maxima = energia_maxima

        #Atributos Privados
        self.__hp_actual = hp_maximo
        self.__energia_actual = energia_maxima
        

