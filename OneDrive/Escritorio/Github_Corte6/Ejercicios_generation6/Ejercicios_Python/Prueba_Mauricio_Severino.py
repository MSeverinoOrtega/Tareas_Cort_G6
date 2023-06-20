
#Cambio de extremos en la Frase
def cambiar_extremos(frase):
    primera_letra = frase[0]
    ultima_letra = frase[-1]
    
    # Verificar si el primer carácter es una minúscula y convertirlo a mayúscula, o viceversa
    if primera_letra.islower():
        primera_letra = primera_letra.upper()
    else:
        primera_letra = primera_letra.lower()
    
    # Verificar si el último carácter es una minúscula y convertirlo a mayúscula, o viceversa
    if ultima_letra.islower():
        ultima_letra = ultima_letra.upper()
    else:
        ultima_letra = ultima_letra.lower()
    
    # Reemplazar el primer y último carácter en la frase
    nueva_frase = primera_letra + frase[1:-1] + ultima_letra
    
    return nueva_frase
#ingreso de la frase
def ingresar_frase():
    while True:
        try:
            frase = input("Ingrese una frase: ")
            if not frase.replace(" ", "").isalpha():
                raise ValueError("La frase solo debe contener letras, espacios, comas y puntos.")
            break
        except KeyboardInterrupt:
            print("no se permiten caidas de sistema")
            return ingresar_frase()
    return frase
#opcion 2 
def Extremos():  
        frase = ingresar_frase()
        nueva_frase = cambiar_extremos(frase)
        print("Frase modificada: " + nueva_frase)
        return retornar()

"-------------------------------------------------------------------------------------"
#Separacion de vocales y consonantes en variables
def separar_vocales_consonantes(frase):
    vocales = ""
    consonantes = ""
    for letra in frase:
        if letra.lower() in "aeiou":
            vocales += letra
        elif letra.isalpha():
            consonantes += letra
    return vocales, consonantes
#ingreso de la frase
def ingresar_frase():
    while True:
        try:
            frase = input("Ingrese una frase: ")
            if not frase.replace(" ", "").isalpha():
                raise ValueError("La frase solo debe contener letras, espacios, comas y puntos.")
            break
        except KeyboardInterrupt:
            print("no se permiten caidas de sistemas")
            return ingresar_frase()
        except ValueError as e:
            print(str(e))
    return frase

#Opcion 1
def separarvocales():  
        frase = ingresar_frase()
        vocales, consonantes = separar_vocales_consonantes(frase)
        print("Vocales: " + vocales)
        print("Consonantes: " + consonantes)
        return retornar()

#Opciones de retorno al finalizar cada funcion
def retornar():
    while True:
        try:
            Retornando = int(input("-------------------------------------------\npara seguir separando vocales ingresa N°1\nPara seguir cambiando extremos ingresa N°2\nPara salir ingresa N°3\nCualquier letra para volver al menu principal\nDigite la opción: "))
            if Retornando == 1:
                return separarvocales()
            elif Retornando == 2:
                return Extremos()
            elif Retornando == 3:
                return salida()
            else:
                return menu()
        except KeyboardInterrupt:
            print("no se permite caida de sistemas")
            return retornar()
            

#Para dar salida a algunos sistemas.
def salida():
        import sys
        sys.exit()

"-------------------------------------------------------------------------------------"
# Función principal del menú
def menu():
    while True:
        print("----------------------------------------------------------------------\n|                             Menú Principal                         |\n----------------------------------------------------------------------\n|1. ingresar frase y mosrar vocales y consonantes por separado       |\n|2. cambiar los extremos a mayuscular o minusculas                   |\n|3. Salir                                                            |\n---------------------------------------------------------------------")
        try:
            opcion = input("Digite la opción: ")
            if opcion == "1":
                    separarvocales()
            elif opcion == "2":     
                    Extremos()
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