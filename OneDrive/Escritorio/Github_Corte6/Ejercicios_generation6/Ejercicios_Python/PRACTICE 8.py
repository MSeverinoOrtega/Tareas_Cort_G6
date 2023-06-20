'''
crear un programa que reciba el numero de años que tiene nuestra computadora 

que vamos a imprimir en consola, si es nuevo o es viejo

condiciones

si es menor o igual a 2 años es nueva

pero si es mayor a 2 años entonces es vieja. 

'''


anios = int(input("cuandotos años tiene tu computadora "))

if anios >= 0 and anios <=2:
    print ("tu computadora es nueva ")
else:
    print("tu computadora es vieja")