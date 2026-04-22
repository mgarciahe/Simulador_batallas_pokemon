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

#Creamos el metodo turno para indicar las acciones a realizar por turno, aca recibe dos obejtos al pokemon y al oponente

def turno(pokemon, oponente):

    print(f"\n--- TURNO DE {pokemon.nombre} ---")

    # Iniciamos con un condicional para verificar si el pokemon esta paralizado
    if pokemon.paralizado:
        pokemon.mostrar_estado()
        print(f"{pokemon.nombre} está paralizado y pierde su turno.")
        #Si el pokemon esta paralizado lo cambiamos a false para cambiar su estado.
        pokemon.paralizado = False
        return

    #Mostramos los datos del pokemon, llamamos al metodo en clase base
    pokemon.mostrar_estado()

    #Creamos un ciclo que corra hasta que el jugador nos brinde una opcion valida
    while True:

        #Usamos try except, indicando ValueError si el jugador ingresa texto en lugar de numero
        try:
            #imprimimos los metodos y que el usuario eliga-
            print("\n1. Atacar (Costo: 15 EP)")
            print("2. Defender (Costo: 5 EP)")
            print("3. Descansar (Restaura: 20 EP)\n")

            opcion = int(input("Opción: "))

            #Usamos el condicional if y si el usuario elige un valor que ejecute su metodo
            # Else por si el usuario ingresa otro numero
            if opcion == 1:
                pokemon.atacar(oponente)
                break

            elif opcion == 2:
                pokemon.defender()
                break

            elif opcion == 3:
                pokemon.descansar()
                break
            
            else:
                print("Opción inválida.")

        except ValueError:
            print("Debes ingresar un número válido.")


