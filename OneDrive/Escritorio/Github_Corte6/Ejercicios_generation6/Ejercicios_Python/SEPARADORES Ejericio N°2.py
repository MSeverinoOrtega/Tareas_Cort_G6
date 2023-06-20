#concatenacion
def concatenacion():
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        print("los numeros de la variable1 y la variable2 concatenados:", str(numero1) + str(numero2))
        return retornarmenu()
    except ValueError:
        print("Solo se permiten valores numéricos")
        return concatenacion()
    except KeyboardInterrupt:
        print("no se permiten cancelaciones de programa")
        return concatenacion()
    except Exception as e:
        print("Error:", str(e))     

#separar 2 mitades de cadenas
def separar_cadenas():
    try:
        palabra = input("Ingrese una palabra: ")
        if palabra.isdigit():
            raise ValueError("Error: No se permiten números.")
        largo = len(palabra)
        mitad = largo//2
        if largo %2 ==0:
            primera_mitad = palabra[:mitad]
            segunda_mitad = palabra[mitad:]
        else:
            primera_mitad = palabra[:mitad + 1]
            segunda_mitad = palabra[mitad + 1:]
        return primera_mitad, segunda_mitad
    except KeyboardInterrupt:
        print("no se permiten cancelaciones de programa")
        return separar_cadenas()
    except Exception as e:
        print("Error:", str(e))    
        return  separar_cadenas()

#Main Calculo de cadenas.
def resultado_cadenas():
    try:
        primera_mitad, segunda_mitad = separar_cadenas()
        print(f'La primera mitad es:, {primera_mitad}, y la segunda mitad es: {segunda_mitad}')
    except KeyboardInterrupt:
        print("no se permiten cancelaciones de programa")

#Seguir programando o salir
def retornarmenu():
    try:
        seguir = int(input("si quieres seguir programando 1 de lo contrario presione cualquier tecla :  "))
        if seguir == 1:
            return menu()
        else:
            print("Cerrando sesión...") #Cerrar sesión y salir. 
            return salida()
    except ValueError:
        print("Cerrando sesión...")
        return salida()
    except  KeyboardInterrupt:
        print("no se permiten caidas de sistema,Cerrando sesión...")
        return salida()

#Para dar salida a algunos sistemas.
def salida():   
        import sys
        sys.exit()

#Menu
def menu():
    while True:
        print("------------------------------------\n|         Menú Principal           |\n------------------------------------\n|1. Concatenación de dos números   |\n|2. Separación de una cadena en dos|\n|3. Salir                          |\n------------------------------------")
        try:
            opcion = input("elige una opcion: ")
            if opcion == "1":
                    concatenacion()
            elif opcion == "2":     
                    resultado_cadenas()
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