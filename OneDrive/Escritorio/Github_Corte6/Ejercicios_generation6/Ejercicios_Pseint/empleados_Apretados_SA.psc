Proceso empleados_Apretados_SA
	// aquí declaramos las variables las cuales almacenarán los datos. 
	suma_sueldo_altos <- 0;
	empl_800 <- 0;
	empl_20milbono <- 0;
	// contabilidad será el marcador de las vueltas del contador.
	contabilidad <- 50;
	Para i<-1 Hasta contabilidad Hacer
		Escribir "ingrese el sueldo correspondiente : " ,i;
		Leer sueldo;
		Escribir "ingrese el bono correspondiente : ", i;
		Leer bono;
		// aquí separamos los que tienen un bono igual a 20.000 mil pesos
		Si bono=20000 Entonces
			// aquí adjuntaremos todas las personas que ganen 20 mil
			// los empl_20milbono, equivalen a 0, por lo tanto por 
			// cada vuelta que vaya pasando se le va sumando el 1
			empl_20milbono <- empl_20milbono+1;
		FinSi
		// Aquí realizaremos la operatoria de cantidad de empleados que ganan sobre 800.000
		// Y tambien realizaremos la suma de los bonos que estén dentro del rango 10 a 15 mi.
		Si sueldo>800000 y bono>=10000 y bono<=15000 Entonces
			// aquí realizaremos la contabilidad de los empleados que cumplen
			// con los 3 requisitos de arriba 
			empl_800 <- empl_800+1;
		FinSi
		// aquí se realizará la suma de los bonos tanto como los de 20 mil, los de 10 y los de 15mil.
		suma_bono <- suma_bono+bono;
		Si sueldo>1500000 Entonces
			// aquí guardaremos todos los sueldos mayores a 1.500.000 pesos 
			suma_sueldo_altos <- suma_sueldo_altos+sueldo;
		FinSi
	FinPara
	// aquí se realizará el promedio lo cual contabilidad promediara con la 
	// cantidad de empleados ingresados dividido por el total de bonos obtenidos por las 3 cantidades
	dividir_bono <- suma_bono/contabilidad;
	Escribir "cantidad de empleados que recibieron un bono de 20.000 mil pesos : ", empl_20milbono;
	Escribir "Cantidad de personas que tienen sueldos superiores a 800000 con bono de 10.000 a 15.000 : ", empl_800;
	Escribir "El promedio de bonos recibidos por los empleados de la emplesa es : ", dividir_bono;
	Escribir " la suma de todos los sueldos superiores a 1.500.000 : ",suma_sueldo_altos;
FinProceso
