Proceso sin_titulo
	CON <- 0;
	conf <- 0;
	sum <- 0;
	X <- 1;
	Mientras (X<=4) Hacer
		Escribir 'nombre';
		Leer nom;
		Escribir 'sex (F/f/M/m)';
		Leer sex;
		Escribir 'sueldo';
		Leer suel;
		Si sex='M' O sex='m' Entonces
			Si suel>800000 Entonces
				CON <- CON+1;
			FinSi
		FinSi
		Si sex='F' O sex='f' Entonces
			conf <- conf+1;
			sum <- sum+suel;
		FinSi
		X <- X+1;
	FinMientras
	Si confi>0 Entonces
		prom <- sum/conf;
	FinSi
	Escribir conf;
	Escribir X;
FinProceso
