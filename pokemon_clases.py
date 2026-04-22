#Importamos del archivo local importamos la clase Pokemon

from ClaseBasePokemon import Pokemon
#Importamos random para utilizarlo con el pokemon Electrico #Se utilizo IA para conocer mas del uso de esta biblioteca
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
        #dano sera igual a daño, pero la computadora de clase no me reconoce la ñ
        dano = 15

        #Usamos la funcion isinstance para indicar si el objeto pertenece a la clase, la usamos con un if
        #Nos indica si el objeto si pertece a esa clase entonces doble daño
        #Agua inflige daño doble (x2) contra Fuego

        if isinstance (oponente, PokemonFuego):
            dano *= 2
            print("¡Es super efectivo!")
    
        #accedemos a los atributos heredados de Clase base y agregamos un if para aplicar daño / 2 si esta en True.
        if oponente.defendiendo:
            dano //= 2
            oponente.defendiendo = False

        #le restamos el daño al oponente
        oponente.hp_actual = oponente.hp_actual - dano
        print(f"{self.nombre} usa un ataque de agua y causa {dano} de daño.")


class PokemonFuego(Pokemon):

    def atacar(self, oponente):

        if self.energia_actual <= 15:
            print(f"{self.nombre} No tiene energia para atacar")
            return

        self.energia_actual -= 15

        #Aca nos basamos en la parte del enunciado que indica:cualquier otra daño normal (x1).        
        dano = 10            

        #Fuego inflige daño doble (x2) contra Planta
        if isinstance(oponente, PokemonPlanta):
            dano *= 2 
            print("¡Es super efectivo!")

        if oponente.defendiendo:
            dano //= 2
            oponente.defendiendo = False

        #le restamos el daño al oponente
        oponente.hp_actual = oponente.hp_actual - dano
        print(f"{self.nombre} ataca y causa {dano} de daño.")


class PokemonPlanta(Pokemon):

    def atacar(self, oponente):

        if self.energia_actual <= 15:
            print(f"{self.nombre} No tiene energia para atacar")
            return

        self.energia_actual -= 15

        dano = 10            

        #Planta inflige daño doble (x2) contra Agua
        if isinstance(oponente, PokemonAgua):
            dano *= 2 
            print("¡Es super efectivo!")

        if oponente.defendiendo:
            dano //= 2
            oponente.defendiendo = False

        oponente.hp_actual = oponente.hp_actual - dano
        print(f"{self.nombre} ataca y causa {dano} de daño.")


class PokemonElectrico(Pokemon):

    def atacar(self, oponente):

        if self.energia_actual <= 15:
            print(f"{self.nombre} No tiene energia para atacar")
            return

        self.energia_actual -= 15

        dano = 10            

        if oponente.defendiendo:
            dano //= 2
            oponente.defendiendo = False

        oponente.hp_actual = oponente.hp_actual - dano
        print(f"{self.nombre} ataca y causa {dano} de daño.")

        #Como se indico al inicio del codigo utilizamos la IA para conocer el uso de la biblioteca random
        # Se utiliza random.random() para generar un numero aleatorio de 0 a 1.
        #Utilizamos un if, para indicar si el valor aleatorio es menor al 0.2 se activa probabilidad del 20%
        if random.random() < 0.2:
            print(f"¡Ataque super efectivo! {oponente.nombre} ha sido paralizado y pierde el siguiente turno")
            oponente.paralizado = True
        else:
            print("El ataque no ha sido muy efectivo")

