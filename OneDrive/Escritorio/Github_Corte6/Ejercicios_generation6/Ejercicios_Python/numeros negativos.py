for i in range(2):
    numero = int(input("Ingrese un número negativo: "))
    if numero < 0:
        numeros_negativos.append(numero)
        if numero >= -100 and numero <= -1:
            rango_1_100.append(numero)
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
        else:
            errores += 1
    else:
        errores += 1

print("Cantidad de números ingresados en el rango de -1 a -100:", len(rango_1_100))
print("Cantidad de números pares en el rango de -1 a -100:", len(pares))
print("Cantidad de números impares en el rango de -1 a -100:", len(impares))
print("Cantidad de ingresos erróneos:", errores)