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
        try:
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
        except Exception:
            print("Entrada invalida, intenta nuevamente")
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
                pokemon.mostrar_estado()
                break

            elif opcion == 2:
                pokemon.defender()
                pokemon.mostrar_estado()
                break

            elif opcion == 3:
                pokemon.descansar()
                pokemon.mostrar_estado()
                break
            
            else:
                print("Opción inválida.")

        except ValueError:
            print("Debes ingresar un número válido.")

#Aca agregamos los datos del turno automatico.
def turno_computadora(pokemon, oponente):

    print(f"\n--- TURNO DE {pokemon.nombre} (Computadora) ---")

    # Iniciamos con un condicional para verificar si el pokemon esta paralizado
    if pokemon.paralizado:
        pokemon.mostrar_estado()
        print(f"{pokemon.nombre} está paralizado y pierde su turno.")
        #Si el pokemon esta paralizado lo cambiamos a false para cambiar su estado.
        pokemon.paralizado = False
        return
    
    pokemon.mostrar_estado()

    #IMPORTANTE, uso de la IA Para conocimiento de la libreria random,
    #random.randint me genera un numero aleatorio entre los valores indicados en parentesis
    opcion = random.randint(1, 3)

    print(f"La computadora elige: {opcion}")

    #Usamos if para verificar el dato elegido aleatoriamente e inicializar los metodos para el valor elegido

    if opcion == 1:
        pokemon.atacar(oponente)
        pokemon.mostrar_estado()

    elif opcion == 2:
        pokemon.defender()
        pokemon.mostrar_estado()

    else:
        pokemon.descansar()
        pokemon.mostrar_estado()


#Creamos el metodo de combate, vamos a indicarle que necesitamos dos parametros jugador 1
#Agregamos un tercer parametro contra_compu, parametro por defecto 
def combate(pokemon_jugador1, pokemon_jugador2, contra_computadora=False):

    print("\n¡COMIENZA LA BATALLA!")
    print(f"{pokemon_jugador1.nombre} vs {pokemon_jugador2.nombre}")

    #Declaramos una variable para identificar a quien le toca jugar
    turno_actual = "jugador1"

    #Creamos un ciclo while para que los jugadores puedan jugar mientras se cumpla la condicion
    while pokemon_jugador1.hp_actual > 0 and pokemon_jugador2.hp_actual > 0:

        print("\n----------------------------------------")

        #Creamos el if, que nos indique si esta el jugador 1, que use el metodo turno, que contiene pokemon y oponente

        if turno_actual == "jugador1":
            #Usamos el metodo turno y le damos los parametros, pokemon = pokemon_jugador1
            turno(pokemon_jugador1, pokemon_jugador2)
            #Cambiamos el valor de turno para que le toque el turno al siguiente jugador
            turno_actual = "jugador2"

        else:
            #Usamos nuestro tercer parametro el cual por ser booleano indicamos contracompu:
            if contra_computadora:
                #Corremos el metodo turno computadora
                turno_computadora(pokemon_jugador2, pokemon_jugador1)
            else:
                #jugagor2
                turno(pokemon_jugador2, pokemon_jugador1)

            #Le devolvemos el valor al siguiente jugador
            turno_actual = "jugador1"

    #Se cierra el ciclo while e indicamos al ganador
        # RESULTADO FINAL
    print("\n========== RESULTADO ==========")

    #Con un ciclo if identificamos si el jugador1 tiene puntos de vida lo cual siginfica es ganador.
    #Sino imprimos jugador2
    if pokemon_jugador1.hp_actual > 0:
        print(f"{pokemon_jugador1.nombre} gana la batalla!")
    else:
        print(f"{pokemon_jugador2.nombre} gana la batalla!")

#Definimos nuestra funcion para mostrar el menu
def main():

    print("======================================")
    print("   SIMULADOR DE BATALLAS POKÉMON")
    print("======================================")

    #Modos de juego
    print("1. Jugador vs Jugador")
    print("2. Jugador vs Computadora")

    #Agregamos la variable que guardara el dato ingresado por el jugador
    modo = input("Selecciona modo: ")

    # llamamos a la funcion importada de pokedex, para mostrar el catalogo
    mostrar_catalogo_disponible()

    # Creamos la variable donde se guardara el pokemon, por lo cual llamamos al metodo elegir pokemon.
    #Le dejamos el nombre pokemon_jugador1 ya que es una variable y no afecta que sea repetido con el nombre de un parametro
    pokemon_jugador1 = elegir_pokemon(1)

    #Condicional si el jugador elige 2, el cpu elige aleatoriamente

    if modo == "2":
        #Uso de IA para corregir el uso de random.choice - uso de la libreria random
        #al utilizar el diccinario.values, nos devuelve los valores, sin la clave.
        #Usamos list, para crear esos valores en una lista
        #Con la lista creada podemos proceder a utilizar random.choice y que nos brinde un valor de las listas
        datos_computadora = random.choice(list(CATALOGO_POKEMON.values()))

        #Creamos la variable donde se guardara el pokemon y llamamos al metodo de crear_pokemon
        #nos brindara datos de diccionario los cuales convertiremos conforme su clase
        pokemon_jugador2 = crear_pokemon(datos_computadora)
        print(f"La computadora eligió a {pokemon_jugador2.nombre}")


        #llamamos al metodo de combate y corremos TRUE contracomputadora
        combate(pokemon_jugador1, pokemon_jugador2, True)

    else:
        # Jugador 2
        pokemon_jugador2 = elegir_pokemon(2)
        combate(pokemon_jugador1, pokemon_jugador2)

main()
