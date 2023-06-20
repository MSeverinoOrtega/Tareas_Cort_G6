def calcular_total(cantidad, valor):
    if cantidad > 3:
        descuento = cantidad * valor
        total_descuento = descuento * 0.9
        return total_descuento
    else:
        descuento = cantidad * valor
        total_descuento = descuento * 0.95
        return total_descuento

def ingresar_datos():
    try:
        cantidad = int(input("Ingrese la cantidad de camisas: "))
        valor = float(input("Ingrese el valor de una camisa: "))
        return cantidad, valor
    except ValueError:
        print("Error: Ingrese un valor válido para la cantidad y el valor de una camisa")
        return None, None

def mostrar_resultado(total):
    if total is not None:
        print("Su total a pagar es:", total)
    else:
        print("No se pudo calcular el total.")

# Uso de las funciones
cantidad, valor = ingresar_datos()
total_a_pagar = calcular_total(cantidad, valor)
mostrar_resultado(total_a_pagar)