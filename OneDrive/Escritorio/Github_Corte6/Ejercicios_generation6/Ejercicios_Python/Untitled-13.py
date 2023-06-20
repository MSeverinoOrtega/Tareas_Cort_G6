def ingresar_numeros():
    numeros = []
    for i in range(2):
        while True:
            try:
                numero = int(input(f"Ingrese el número {i+1}: "))
                if numero > 0:
                    numeros.append(numero)
                    break
                else:
                    print("Error: Ingrese un número positivo.")
            except ValueError:
                print("Error: Ingrese un número válido.")
    return numeros


def contar_en_rango(numeros):
    contador = 0
    for numero in numeros:
        if 30 <= numero <= 100:
            contador += 1
    return contador


def verificar_divisibilidad(numeros):
    contador_divisibles = 0
    for numero in numeros:
        if numero % 5 == 0:
            contador_divisibles += 1
    return contador_divisibles

# Flujo principal del programa
try:
    numeros_ingresados = ingresar_numeros()
    numeros_en_rango = contar_en_rango(numeros_ingresados)
    numeros_divisibles = verificar_divisibilidad(numeros_ingresados)

    print(f"Números encontrados en el rango de 30 a 100: {numeros_en_rango}")
    print(f"Números divisibles por 5: {numeros_divisibles}")

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario.")

except Exception as e:
    print(f"Error: {str(e)}")