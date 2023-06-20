Proceso promedio_notas
	p <- 0;
	sum <- 0;
	x <- 1;
	Mientras x<=4 Hacer
		Escribir "ingrese nota ", x;
		Leer NOTA;
		sum <- sum+NOTA;
		x <- x+1;
	FinMientras
	p <- sum/x;
	Escribir "el promedio fue ", p;
FinProceso
