cantidad = int(input("Ingrese la cantidad de camisas: "))
valor = float(input("Ingrese el valor de una camisa: "))


if cantidad > 3:
    descuento = cantidad * valor
    print(f"su total es:",descuento)
    print(f"se le aplicara un descuento de 10%"," Su total a pagar es:",descuento*0.90)
else:
    descuento = cantidad * valor
    print(f"su total es: {descuento}")
    print(f"se le aplicara un descuento de 5% ",descuento*0.95)
