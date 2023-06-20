def calcular_total(camisas, valor_camisa):
    try:
        camisas = int(camisas)
        valor_camisa = float(valor_camisa)

        subtotal = camisas * valor_camisa

        if camisas >= 3:
            descuento = subtotal * 0.1
        else:
            descuento = subtotal * 0.05

        total = subtotal - descuento
        return total
    except ValueError:
        return "Error: Ingrese un valor válido para la cantidad de camisas y el valor de una camisa"


def main():
    cantidad = input("Ingrese la cantidad de camisas: ")
    valor = input("Ingrese el valor de una camisa: ")

    total_a_pagar = calcular_total(cantidad, valor)
    print(total_a_pagar)
    
    
if __name__ == "__main__":
    main()