# Inicializar variables
productos = []
precios = []
stocks = []

# Ingresar datos de productos, precios y stocks
for i in range(20):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad de stock del producto: "))

    # Validar que precio y stock sean mayores a 0
    while precio <= 0 or stock <= 0:
        print("Error: el precio y el stock deben ser mayores a 0.")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese la cantidad de stock del producto: "))

    # Agregar datos a las listas
    productos.append(nombre)
    precios.append(precio)
    stocks.append(stock)

# a) Cantidad de productos con stock > 15
cant_stock_mayor_15 = 0
for stock in stocks:
    if stock > 15:
        cant_stock_mayor_15 += 1
print(f"Cantidad de productos con stock mayor a 15: {cant_stock_mayor_15}")

# b) Producto con mayor precio
max_precio = max(precios)
indice_max_precio = precios.index(max_precio)
producto_max_precio = productos[indice_max_precio]
print(f"Producto con mayor precio: {producto_max_precio}")