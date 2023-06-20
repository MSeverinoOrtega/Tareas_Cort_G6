Proceso sin_titulo
	// Se pide al usuario ingresar la cantidad de estudiantes
	Escribir 'Ingrese la cantidad de estudiantes:';
	Leer cantidadEstudiantes;
	// Variables para contabilizar los estudiantes por nota
	nota4 <- 0;
	nota5 <- 0;
	nota6 <- 0;
	nota7 <- 0;
	// Ciclo para ingresar los puntajes de los estudiantes
	Para i<-1 Hasta cantidadEstudiantes Hacer
		puntaje <- -1; // Inicializamos puntaje con valor inválido
		// Ciclo para asegurarnos que el puntaje ingresado es válido
		Mientras puntaje<3 O puntaje>20 Hacer
			Escribir 'Ingrese el puntaje del estudiante ',i,':';
			Leer puntaje;
			Si puntaje<3 O puntaje>20 Entonces
				Escribir 'Puntaje inválido. Intente nuevamente.';
			FinSi
		FinMientras
		Segun puntaje  Hacer
			9,10,11:
				nota4 <- nota4+1;
			12,13,14:
				nota5 <- nota5+1;
			15,16,17:
				nota6 <- nota6+1;
			18,19,20:
				nota7 <- nota7+1;
		FinSegun
	FinPara
	// Convertimos el puntaje a nota y lo contabilizamos
	// Mostramos los resultados
	Escribir 'Cantidad de estudiantes con nota 4:',nota4;
	Escribir 'Cantidad de estudiantes con nota 5:',nota5;
	Escribir 'Cantidad de estudiantes con nota 6:',nota6;
	Escribir 'Cantidad de estudiantes con nota 7:',nota7;
FinProceso
