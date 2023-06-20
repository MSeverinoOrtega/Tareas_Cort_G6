
cadena_dos = ""
vocal = ""

#Aqui definimos el comportamiento del menu
def menu():
    print("-----------------------------------------------------------------------------\n|        			Menú Principal   			    |\n-----------------------------------------------------------------------------\n|   1.- Combinación de palabras                              		    |\n|   2.- Contar vocal en texto ingresado				            |\n|   3.-  Salir							            |\n-----------------------------------------------------------------------------")
    try:
        opcion = 0
        while opcion == 0:
            opcion = int(input("Ingrese opción del menú a la que desea ingresar: "))
            if opcion == "":
                print("Opción no válida, por favor ingresa un número")
                return menu()
            elif opcion <= 0 or opcion >=4:
                print("Opción no válida, por favor escoja el número de la opción acorde a su solicitud")
                return menu()
        if opcion == 1:
            return combinar()
        elif opcion == 2:
            return conteo_vocal()
        elif opcion == 3:
            print("¡Hasta pronto!")
    except KeyboardInterrupt:
        print("Solo se permiten valores numéricos")
        return menu()      
    except ValueError:
        print("Solo se permiten valores numéricos")
        return menu()
    except:
        print("Por favor ingrese el número de opción indicado en el menú")
        return menu()
#OPCION 1
#Aqui definimos le recursividad de la opcion 1    
def regreso1():
    try:
        opcion = int(input("Si desea combinar más palabras indique opcion 1, si desea regresar al menú indique opción 0: "))
        if opcion == "":
            print("No se permiten espacios vacios, por favor ingresa un número")
        elif 0 < opcion > 1:
            print("Por favor escoja el número de la opción acorde a su solicitud")
            return regreso1()
        elif opcion == 1:
            return combinar()
        elif opcion == 0:
            return menu()
    except KeyboardInterrupt:
        print("Solo se permiten valores numéricos")
        return regreso1()  
    except ValueError:
        print("Solo se permiten valores numéricos")
        return regreso1() 
    except:
        print("Solo se permiten valores numéricos")
        return regreso1() 
        
#Aqui realizamos la combinacion de letras segun la opcion 1
def combinar():
    try:
        cadena1 = input("Ingrese la primera palabra a combinar: ")
        cadena1 = cadena1.replace(" ", "")    
        if cadena1 == "":
            print("No se permiten espacios vacios, por favor ingresa un número")   
            return combinar() 
    except KeyboardInterrupt:
        print("Solo se permiten valores numéricos")
        return combinar() 
    except:
        print("Error, por favor ingrese letras o numeros")
        return combinar() 
    
    try:
        cadena2 = input("Ingrese la segunda palabra a combinar: ")
        cadena2 = cadena2.replace(" ", "")
        if cadena2 == "":
            print("No se permiten espacios vacios, por favor ingresa un número")
            return combinar()
    except KeyboardInterrupt:
        print("\nSolo se permiten valores numéricos")
        return combinar()        
    except:
        print("Error, por favor ingrese letras o numeros")
        return combinar()
  
    resultado = ""
    x = 0
    y = 0

    if len(cadena2) > len(cadena1):
        cadena1, cadena2 = cadena2, cadena1
        
    while x < len(cadena2):
        resultado += cadena1[x] + cadena2[x]
        x += 1  
    resultado += cadena1[len(cadena2):]
    print(resultado) 
    regreso1()

#OPCION 2
#Aca realizamos la verificación de datos para correr opcion 2
def verificar_cadena():
        try:
            global cadena_dos
            cadena_dos = input("Ingrese una frase: ")
            if cadena_dos == "":
                print("No se permiten espacios vacios, por favor ingresa una frase")
                return verificar_cadena()
            for caracter in cadena_dos:
                if caracter in ['á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú']:
                    print("El texto no puede contener tildes")
                    return verificar_cadena()
        except KeyboardInterrupt:
            print("Por favor ingrese letras o numeros")
        except:
            print("Por favor ingrese letras o numeros")
        return cadena_dos

def verificar_vocal():
    try:
        global vocal
        vocal = input("Ingrese la vocal a buscar: ")
        if vocal == "":
            print("No se permiten espacios vacios, por favor ingresa un número")
            return verificar_vocal()
        for caracter in vocal:
            if caracter in ['á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú']:
                print("El texto no puede contener tildes")
                return verificar_vocal()
    except KeyboardInterrupt:
        print("Solo se permiten valores numéricos")
        return menu()            
    except:
        print("Por favor ingrese letras o numeros")
        return verificar_vocal()
    return vocal
#Aqui definimos le recursividad de la opcion 2
def regreso2():
    try:
        opcion = int(input("Si desea contar más vocales indique opcion 1, si desea regresar al menú indique opción 0: "))
        if opcion == "":
            print("No se permiten espacios vacios, por favor ingresa un número")
        elif 0 < opcion > 1:
            print("Por favor escoja el número de la opción acorde a su solicitud")
            return regreso1()
        elif opcion == 1:
            return conteo_vocal()
        elif opcion == 0:
            return menu()
    except KeyboardInterrupt:
        print("Solo se permiten valores numéricos")
        return menu()  
    except ValueError:
        print("Solo se permiten valores numéricos")
#Aqui realizamos el conteo de letras segun la opcion 2  
def conteo_vocal():
    cadena3 = verificar_cadena()
    vocal2 = verificar_vocal()
    
    cantidad = 0
    indice = 0
    while indice < len(cadena3.lower):
        caracter = cadena3[indice]
        if caracter.lower() == vocal2.lower:
            cantidad += 1
        indice += 1
    if cantidad > 0:
        print(f"La vocal {vocal2} fue encontrada en {cantidad} de posición(es)")
    regreso2()

menu()