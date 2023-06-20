# Función para combinar palabras

        #el .Strip() nos permite eliminarás los espacios en blanco alrededor de la palabra ingresada, lo que garantiza que no se acepten palabras que 
        # consistan únicamente en espacios en blanco. De esta manera, si el usuario ingresa solo espacios en blanco, se considerará como una cadena vacía 
        # y se mostrará el mensaje correspondiente.
    #not nuestra variable.isalpha():      Esto sirve para evitar todo lo que no sea palabra
    
    
    
def combinar():
    
    palabra1 = ""
    try:
        while palabra1 == "" or not palabra1.isalpha():
            palabra1 = input("Ingrese la primera palabra: ").strip()
            if palabra1 == "" or not palabra1.isalpha():
                print("No has ingresado una palabra")
    except:
        print("Error, Ingrese solo letras")
        
        
    try:   
        palabra2 = input("Ingrese la segunda palabra: ")
        if palabra2 == "":
            raise ValueError("Error: No se permiten cadenas vacías.")
        
        
        
        
        
        if palabra1 and palabra2:
            if len(palabra1) >= len(palabra2):
                resultado = ''.join([a + b for a, b in zip(palabra1, palabra2)])
                resultado += palabra1[len(palabra2):]
            else:
                resultado = ''.join([a + b for a, b in zip(palabra2, palabra1)])
                resultado += palabra2[len(palabra1):]
            
            print("La combinación de las palabras es:", resultado)
        else:
            print("Error: No se permiten cadenas vacías.")
    except Exception as e:
        print("Error:", str(e))


# Función para contar vocales en un texto
def conteoVocal():
    texto = input("Ingrese un texto: ")
    vocal = input("Ingrese una vocal: ")

    try:
        if texto and vocal:
            if vocal.lower() not in ['a', 'e', 'i', 'o', 'u']:
                print("Error: Ingrese una vocal válida (sin tildes).")
                return

            contador = sum(1 for char in texto if char.lower() == vocal.lower())
            if contador == 0:
                print("La vocal", vocal, "no fue encontrada.")
            else:
                print("La vocal", vocal, "fue encontrada en", contador, "posición(es).")
        else:
            print("Error: No se permiten textos o vocales vacías.")
    except Exception as e:
        print("Error:", str(e))


# Función principal del menú
def menu():
    while True:
        print("----------------------------------\n|        Menú Principal            |\n----------------------------------\n|1. Combinación de palabras        |\n|2. Contar vocal en texto ingresado|\n|3. Salir                          |\n-----------------------------------")

        opcion = input("Digite la opción: ")

        try:
            if opcion == "1":
                combinar()
            elif opcion == "2":
                conteoVocal()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("OPCIÓN NO VÁLIDA")
        except Exception as e:
            print("Error:", str(e))


# Llamada a la función principal del menú
menu()