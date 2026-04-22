#Importamos nuestros archivos.
#Importamos nuestro catologo de pokemon y el metodo mostrar catalogo
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
#Importamos nuestro archivo con las clases de pokemon
from pokemon_clases import PokemonAgua, PokemonFuego, PokemonPlanta, PokemonElectrico


import random

#Creamos el pokemon, En el metodo elegir pokemon vamos a solicitar los datos del diccionario

def crear_pokemon(datos):

    #extraemos el tipo de Pokemon del diccionario

    tipo = datos["tipo"]

    #Realizamos la instanciacion del objeto. el objeto se crea conforme a su clase.
    #Usamos un condicional para que nuestro objeto se cree conforme a su clase.

    if tipo == "Agua":
        return PokemonAgua(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

    elif tipo == "Fuego":
        return PokemonFuego(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

    elif tipo == "Planta":
        return PokemonPlanta(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

    elif tipo == "Electrico":
        return PokemonElectrico(datos["nombre"], datos["hp_maximo"], datos["energia_maxima"])

#Elegimos al pokemon, agregamos el paremetro jugador para que nos indique que pokemon desea
def elegir_pokemon(jugador):

    #Con ciclo while dejamos que el jugador ingrese el numero correcto de lo contrario le damos el error
    while True:
        
        #agregamos el valor opcion para verificar si el dato que el jugador esta ingresando esta en el diccionario
        opcion = input(f"Jugador {jugador}, elige el número de tu Pokémon: ")

        #Si el dato ingresado esta en el catalogo, el parametro datos extrae la informacion del diccionario catalogo
        #creamos la variable pokemon el cual traera al metodo crear_pokemon
        if opcion in CATALOGO_POKEMON:
            datos = CATALOGO_POKEMON[opcion]
            pokemon = crear_pokemon(datos)
            print(f"¡Has seleccionado a {pokemon.nombre}!")
            return pokemon
        else:
            print("Opción inválida. Intenta de nuevo.")

