from __future__ import print_function
from dex import get_pokemon_data, get_pokemon_learnset, get_move
import os, sys

print ("Bienvenido")
name_pokemon = ""


pokedex_on = True
while(pokedex_on):
    name_pokemon = input("Ingrese el nombre del Pokémon: ")
    name_pokemon = name_pokemon.lower()
    os.system('clear')
    pokemon = get_pokemon_data(name_pokemon) #E
    '''
    * La función 'get_pokemon_data' recibe un str y devuelve un diccionario con los datos de el Pokémon consultado
    * Las llaves que contiene el diccionario son las siguiente:
        {
            "num" -> Número del Pokémon
            "species"-> Nombre del Pokémon
            "types" -> Lista que contiene el o los Tipos del Pokémon ejemplo: ["Grass", "Poison"],
            "genderRatio" -> Contiene un diccionario con valores float que determina la probabilidad de aparición en la hierba
                                ejemplo: { "M": 0.875, "F": 0.125 },
            "gender": -> Contiene un valor str y solo indica que el Pokémon es de un sólo genero, Ejemplo: "N",
                            esta llave puede tener los siguientes valores: N (Neutral), F (Femenino) y M (Masculino)
            "baseStats" -> Esta llave contiene un diccionario con valores int y representan los stats base hp, ataque, defensa, ataque especial, defensa especial y velocidad
                            Ejemplo: { "hp": 45, "atk": 49, "def": 49, "spa": 65, "spd": 65, "spe": 45 },
            "abilities" -> Esta llave contiene un diccionario con las habilidades, Ejemplo: { "0": "Overgrow", "H": "Chlorophyll" },
            "heightm" -> Esta llave contiene un valor float la cual muestra la altura del Pokémon en metros, Ejemplo: 0.7,
            "weightkg" -> Esta llave contiene un valor float la cual muestra el peso en kilos del Pokémon, Ejemplo: 6.9,
            "color" -> Esta llave contiene un valor str indicando el color primario del Pokémon, Ejemplo: "Green",
            "evos" -> Contiene una lista de valores str que almacena las siguientes evoluciones del Pokémon, Ejemplo: ["ivysaur"],
            "eggGroups" -> Contiene la el grupo de huevo del Pokémon y es una lista con valores str, Ejemplo ["Monster", "Grass"],
            "otherFormes" -> Contiene una lista con valores str en su interior y muestra las formas regionales o mega evoluciones del Pokémon
                            Ejemplo: ["exeggutoralola"] o ["latiosmega"]
        }
    * Nota: Algunas llaves pueden tanto existir como no existir en el diccionario devuelto, por lo que 
            se recomineda verificar verificar si la llave existe en el diccionario
    '''
    if pokemon is not None: # Si lo que devuelve la funcion get_pokemon_data no es None entonces muestra la información
        # Muestra los datos principales del Pókemon        
        print ("\nPokémon número ", pokemon['num']) # Número del Pokémon
        print ("\nNombre del Pokémon: ", pokemon['species']) #Nombre del Pokémon
        print ("\nSus tipos son: ")
        for pokemon_type in pokemon["types"]: # Se recorre la lista e imprime en pantalla los tipos
            print("  - ",pokemon_type)

        if "baseStats" in pokemon: # Se verifica si la llave existe
            print("\nEstadísticas base del Pokémon: ")
            print("  - HP = ", (pokemon["baseStats"]["hp"])) 
            print("  - Ataque = ",(pokemon["baseStats"]["atk"])) 
            print("  - Defensa = ", (pokemon["baseStats"]["def"])) 
            print("  - Ataque especial = ",(pokemon["baseStats"]["spa"])) 
            print("  - Defensa especial = ", (pokemon["baseStats"]["spd"])) 
            print("  - Velocidad = ",(pokemon["baseStats"]["spe"])) 

        if "genderRatio" in pokemon: # Se verifica si la llave existe
            print("\nPosibilidad de aparición según género: ")
            print("  - Macho = ", (pokemon["genderRatio"]["M"] * 100), "%") 
            print("  - Hembra = ",(pokemon["genderRatio"]["F"] * 100), "%") 

        elif "gender" in pokemon: # Si no exite se verifica la segunda posibilidad, de lo contrario no se muestra
            print("\nGénero único:")
            if pokemon["gender"] == "N":
                print("  - Neutral")

            elif pokemon["gender"] == "F":
                print("  - Hembra")

            elif pokemon["gender"] == "M":
                print("  - Macho")
        
        if "evos" in pokemon: # Se verifica si el Pokémon tiene evoluciones
            print("\nSiguiente evolución: ")
            for evo in pokemon["evos"]: # Si tiene evoluciones se recorre la lista y se imprime su nombre
                pokemon_evo = get_pokemon_data(evo)
                print("  - ", pokemon_evo["species"])

        if "otherFormes" in pokemon: # Se verifica si el Pokémon posee otra forma regional y/o Mega evolución
            print("\nOtras formas del Pokémon: ")
            for other_form in pokemon["otherFormes"]:# Si es verdadero se consulta la información
                form_pokemon = get_pokemon_data(other_form)                
                new_name_pokemon = str(form_pokemon["species"]).split('-')
                print ("  - ", new_name_pokemon[1], new_name_pokemon[0])

        print('\nMovimientos que puede aprender el pokémon: ')
        for move in get_pokemon_learnset(name_pokemon):
            print('  - ', str(get_move(move)['name']))
    else:# En caso de que no se encuentre el Pokémon muestra un muestra un mensaje de no encontrado
        print("Pokemon no encontrado")

    

