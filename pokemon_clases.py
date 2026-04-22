#Importamos del archivo local importamos la clase Pokemon

from ClaseBasePokemon import Pokemon
#Importamos random para utilizarlo con el pokemon Electrico
import random   

#creamos las diferentes clases de pokemon, estas son las clases hijas
class PokemonAgua(Pokemon):

    #Heredamos el metodo atacar y lo modificamos, atacar costo de energia es 15
    def atacar(self, oponente):
        if self.energia_actual < 15:
            print(f"{self.nombre} No tiene energia para atacar")
            return
    #dentro del metodo reducimos la energia
        self.energia_actual -= 15
        #agregamos una variable daño, daño sera de 15.
        #Siguiendo el ejemplo Squirtle (Agua) vs Charmander (Fuego), vemos que daño es de 30, por lo cual su valor sera de 15
        
        dano = 15

        #Usamos la funcion isinstance para indicar si el objeto pertenece a la clase, la usamos con un if
        #Nos indica si el objeto si pertece a esa clase entonces doble daño

        if isinstance (oponente, PokemonFuego):
            dano *= 2
            print("¡Es super efectivo!")
    
        #accedemos a los atributos heredados de Clase base y agregamos un if para aplicar daño / 2 si esta en True.
        if oponente.defendiendo:
            dano //= 2
            oponente.defendiendo = False

        #le restamos el daño al oponente
        oponente.hp_actual = oponente.hp_actual - dano





class PokemonFuego(Pokemon):

    def atacar(self):

class PokemonPlanta(Pokemon):

    def atacar(self):

class PokemonElectrico(Pokemon):

    def atacar(self):
