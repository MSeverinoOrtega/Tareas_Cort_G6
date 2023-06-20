def ingresarNumero():
    global numError
    try:
        num = int(input("Ingrese un numero: "))
        
        if num>= 0:
            numError+=1
            print("Debe ingresar solo números negativos")
            return ingresarNumero()
        else:
            return num
    except:
        print("Debe ingresar un número...")
        return ingresarNumero()
def calculos(num):
    global numRango, numPar, numImpar
    if -100<= num <= -1:
        numRango +=1
        if num % 2 ==0:
            numPar +=1
        else:
            numImpar +=1
def desplegar():    
    print("Fueron ingresados ", numRango, " numeros en el rango de -1 y -100.")
    print(numPar, " fueron pares.")
    print(numImpar, " fueron impares.")
    print(numError, " fueron numeros erroneos (positivos/neutros).")
cont = 1
numRango = 0
numPar = 0
numImpar = 0
numError = 0
while cont<=2:
    num = ingresarNumero()
    calculos(num)
    cont +=1
print ()
desplegar()