Proceso sin_titulo
	sumaBono20000 <- 0;
	sumaBono <- 0;
	cantidadEmpleadosSueldoMayor800000 <- 0;
	sumaSueldosSuperiores1500000 <- 0;
	cantidadEmpleados <- 3;
	contador <- 1;
	Mientras contador<=cantidadEmpleados Hacer
		Escribir 'Ingrese el sueldo del empleado ',contador,': ';
		Leer sueldo;
		Escribir 'Ingrese el bono del empleado ',contador,': ';
		Leer bono;
		Si bono=20000 Entonces
			sumaBono20000 <- sumaBono20000+1;
		FinSi
		Si sueldo>800000 Y bono>=10000 Y bono<=15000 Entonces
			cantidadEmpleadosSueldoMayor800000 <- cantidadEmpleadosSueldoMayor800000+1;
		FinSi
		sumaBono <- sumaBono+bono;
		Si sueldo>1500000 Entonces
			sumaSueldosSuperiores1500000 <- sumaSueldosSuperiores1500000+sueldo;
		FinSi
		contador <- contador+1;
	FinMientras
	promedioBono <- sumaBono/cantidadEmpleados;
	Escribir 'Cantidad de empleados que recibieron un bono de 20000 mil pesos: ',sumaBono20000;
	Escribir 'Cantidad de empleados con sueldos mayores a 800000 mil pesos y un bono entre 10000 y 15000 mil pesos: ',cantidadEmpleadosSueldoMayor800000;
	Escribir 'Promedio de bonos recibidos por los empleados de la empresa: ',promedioBono;
	Escribir 'Suma de sueldos superiores a 1500000 mil pesos: ',sumaSueldosSuperiores1500000;
FinProceso
