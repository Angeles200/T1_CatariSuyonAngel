import random

# Clase para guardar  el nombre del entrenador
class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase del pokemon 
class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.vida_max = random.randint(150, 400)
        self.vida_actual = self.vida_max  # empieza igual

    def recuperar(self):
        


        self.vida_actual = self.vida_max

# Variables para el jugador
entrenador1 = None
pokemon1 = None
ganadas = 0
perdidas = 0

# Función para crear entrenador y su pokemon
def crearEntrenadorPokemon(num):
    global entrenador1, pokemon1

    if num == 1:
        print("Creando tu entrenador y pokemon:")
        nombre_ent = input("Nombre del entrenador: ")
        nombre_poke = input("Nombre del pokemon: ")
        entrenador1 = Entrenador(nombre_ent)
        pokemon1 = Pokemon(nombre_poke)
        print("Tu pokemon tiene:")
        print("Ataque maximo:", pokemon1.max_ataque)
        print("Vida maxima:", pokemon1.vida_max)
    else:
        print("Creando entrenador y pokemon rival:")
        nombre_ent = input("Nombre del entrenador rival: ")
        nombre_poke = input("Nombre del pokemon rival: ")
        entrenador2 = Entrenador(nombre_ent)
        pokemon2 = Pokemon(nombre_poke)
        print("El pokemon rival tiene:")
        print("Ataque maximo:", pokemon2.max_ataque)
        print("Vida maxima:", pokemon2.vida_max)
        return entrenador2, pokemon2

# Función para calcular un ataque
def valorDeAtaque(pokemon):
    return random.randint(0, pokemon.max_ataque)

# Función para defenderse
def defender(pokemon_defensor, ataque):
    dado = random.randint(1, 6)
    if dado == 6:  # si sale 6, no recibe daño
        ataque = 0
    pokemon_defensor.vida_actual -= ataque
    return pokemon_defensor.vida_actual

# Menú 


def menu():
    print("\n--- MENU ---")
    print("P = Pelear")
    print("F = Finalizar")
    return input("Elige opcion: ").upper()


crearEntrenadorPokemon(1)  #  se crea el jugador

while True:
    opcion = menu()

    if opcion == "P":
        # Recuperar vida del pokemon del jugador antes de pelear
        pokemon1.recuperar()

        # Crear enemigo
        entrenador2, pokemon2 = crearEntrenadorPokemon(2)

        # Se turnan los ataques
        turno = 1  # 1 ataca primero
        while pokemon1.vida_actual > 0 and pokemon2.vida_actual > 0:
            if turno == 1:
                ataque = valorDeAtaque(pokemon1)
                vida_restante = defender(pokemon2, ataque)
                print(f"\n{pokemon1.nombre} ataca con {ataque}")
                print(f"Vida del rival ahora: {vida_restante}")
                turno = 2
            else:
                ataque = valorDeAtaque(pokemon2)
                vida_restante = defender(pokemon1, ataque)
                print(f"\n{pokemon2.nombre} ataca con {ataque}")
                print(f"Tu vida ahora: {vida_restante}")
                turno = 1

        # Ver quién ganó
        if pokemon2.vida_actual <= 0:
            print("\nGanaste la pelea!")
            ganadas += 1
        else:
            print("\nPerdiste la pelea!")
            perdidas += 1

    elif opcion == "F":
        # Resultado final
        print("\n--- RESULTADOS ---")
        print("Entrenador:", entrenador1.nombre)
        print("Pokemon:", pokemon1.nombre)
        print("Ataque max:", pokemon1.max_ataque)
        print("Vida max:", pokemon1.vida_max)
        print("Peleas ganadas:", ganadas)
        print("Peleas perdidas:", perdidas)
        break
    else:
        print("Opcion incorrecta.")
