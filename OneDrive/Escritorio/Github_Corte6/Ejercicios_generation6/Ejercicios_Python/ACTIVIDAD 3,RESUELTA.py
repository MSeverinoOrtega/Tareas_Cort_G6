# se utiliza la función ord() para obtener los valores ASCII de 
# las letras ingresadas por el usuario en las variables 
# .isdigit() para validad que sea solo letras. raise evaluerror(error no se permiten numeros)
#except Exception as e: para devolver cualquier tipo de error a nuestra def

#Def 2 : usamos el lower para conertir toda la frase a minuscula
#Def 2 : 


def determinar_letra_mayor():
    try:
        letra1 = input("Ingrese la primera letra: ")
        letra1 = letra1.replace(" ","")
        if letra1 == "":
            print("No se permiten espacios vacios")
            return determinar_letra_mayor()
        if letra1.isdigit():
            raise ValueError("Error: No se permiten números.")
        letra2 = input("Ingrese la segunda letra: ")
        letra2 = letra2.replace(" ","")
        if letra2 == "":
            print("No se permiten espacios vacios")
        if letra2.isdigit():
            raise ValueError("Error: No se permiten números.")
# Obtener los valores ASCII de las letras
        valor_ascii_letra1 = ord(letra1)
        valor_ascii_letra2 = ord(letra2)
        if valor_ascii_letra1 > valor_ascii_letra2:
            print("La letra", letra1, "es mayor que la letra", letra2)
        elif valor_ascii_letra1 < valor_ascii_letra2:
            print("La letra", letra2, "es mayor que la letra", letra1)
        else:
            print("Las letras", letra1, "y", letra2, "son iguales")
    except KeyboardInterrupt:
                print("no se permiten caidas de sistemas")
                return determinar_letra_mayor()
    except Exception as e:
        print("Error:", str(e))    
        return  determinar_letra_mayor()

def letra_ingresada():
    try:
        frase = input("Ingrese una frase: ")
        if frase.isdigit():
            raise ValueError("Error: No se permiten números.")
        frase = frase.lower()
# Crear una lista de tuplas con la letra y su cantidad de apariciones
        contador_letras = [(letra, frase.count(letra)) for letra in set(frase) if letra.isalpha()]
# Encontrar la letra con la mayor cantidad de apariciones
        letra_mas_ingresada = max(contador_letras, key=lambda x: x[1])
        print("La letra", letra_mas_ingresada[0], "fue la más ingresada con un total de", letra_mas_ingresada[1], "apariciones.")
    except KeyboardInterrupt:
        print("no se permiten interrupciones de programa0")
        return letra_ingresada()
    except Exception as e:
        print("Error:", str(e))    
        return  letra_ingresada()

#Menu
def menu():
    while True:
        print("------------------------------------\n|           Menú Principal           |\n------------------------------------\n|1. Determinar letra mayor           |\n|2. Letra más ingresada en una frase |\n|3. Salir                            |\n------------------------------------")
        try:
            opcion = input("elige una opcion: ")
            if opcion == "1":
                    determinar_letra_mayor()
            elif opcion == "2":     
                    letra_ingresada()
            elif opcion == "3":
                    print("¡Hasta luego!")
                    break
            else:
                    print("OPCIÓN NO VÁLIDA")
        except ValueError:
            print("solo se permite valores del 1 al 3")
        except KeyboardInterrupt:
                print("solo se permiten valores del 1 al 3")
                return menu()
# Llamada a la función principal del menú
menu()