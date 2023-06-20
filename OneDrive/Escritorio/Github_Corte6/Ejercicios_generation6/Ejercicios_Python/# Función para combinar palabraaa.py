# Función para combinar palabras

        #el .Strip() nos permite eliminarás los espacios en blanco alrededor de la palabra ingresada, lo que garantiza que no se acepten palabras que 
        # consistan únicamente en espacios en blanco. De esta manera, si el usuario ingresa solo espacios en blanco, se considerará como una cadena vacía 
        # y se mostrará el mensaje correspondiente.
    #not nuestra variable.isalpha():      Esto sirve para evitar todo lo que no sea palabra
    
#combinacion de palabras
def combinar():
    
    try:
        palabra1 = input("Ingrese la primera palabra: ")
        palabra1 = palabra1.replace(" ","")
        if palabra1 == "":
            print("No has ingresado una palabra")
            return combinar()
    except KeyboardInterrupt:
            print("no se permite cancelar programa")
    except:
        print("Error, Ingrese solo letras")
        return combinar()
    try:   
        palabra2 = input("Ingrese la segunda palabra: ")
        palabra2 = palabra2.replace(" ","")
        if palabra2 == "":
            print("Error: No se permiten cadenas vacías.")
            return combinar()
        
        if palabra1 and palabra2:
            if len(palabra1) >= len(palabra2):
                resultado = ''.join([a + b for a, b in zip(palabra1, palabra2)])
                resultado += palabra1[len(palabra2):]
            else:
                resultado = ''.join([a + b for a, b in zip(palabra2, palabra1)])
                resultado += palabra2[len(palabra1):]
            
            print("La combinación de las palabras es:", resultado)
            return retornarmenu()
        else:
            print("Error: No se permiten cadenas vacías.")
    except KeyboardInterrupt:
        print("no se permiten cancelaciones de")
    except Exception as e:
        print("Error:", str(e))


# Función para contar vocales en un texto
def conteoVocal():
    try:
        global texto,vocal
        texto = input("Ingrese un texto: ")
        vocal = input("Ingrese una vocal: ")
        if texto and vocal:
            if vocal.lower() not in ['a', 'e', 'i', 'o', 'u']:
                print("Error: Ingrese una vocal válida (sin tildes) y recuerde que el conteo solo es de las vocales.")
                return conteoVocal()
            contador = sum(1 for char in texto if char.lower() == vocal.lower())
            if contador == 0:
                print("La vocal", vocal, "no fue encontrada.")
            else:
                print("La vocal", vocal, "fue encontrada en", contador, "posición(es).")
        else:
            print("Error: No se permiten textos o vocales vacías.")
    except Exception as e:
        print("Error:", str(e))
    except KeyboardInterrupt:
        print("no se permite cancelar el programa")
        return conteoVocal()

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
        print("no se permiten caidas de sistema")
    
#Para dar salida a algunos sistemas.
def salida():
        import sys
        sys.exit()
        
# Función principal del menú
def menu():
    while True:
        print("----------------------------------\n|        Menú Principal            |\n----------------------------------\n|1. Combinación de palabras        |\n|2. Contar vocal en texto ingresado|\n|3. Salir                          |\n-----------------------------------")
        try:
            opcion = input("Digite la opción: ")
            if opcion == "1":
                    combinar()
            elif opcion == "2":     
                    conteoVocal()
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