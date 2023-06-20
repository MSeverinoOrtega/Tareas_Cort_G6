Proceso Notas
	// Declaración de variables
	// Inicialización de variables
	nota_4 <- 0;
	nota_5 <- 0;
	nota_6 <- 0;
	nota_7 <- 0;
	// Lectura de la cantidad de estudiantes
	Escribir 'Ingrese la cantidad de estudiantes:';
	Leer cant_estudiantes;
	// Ciclo para ingresar los puntajes y calcular las notas
	Para i<-1 Hasta cant_estudiantes Hacer
		// Lectura del puntaje
		Escribir 'Ingrese el puntaje del estudiante  ',i,' (este debe ser entre 4 a 20 puntos):';
		Leer puntaje;
		// Aquí verificaremos que nuestro puntaje esté dentro del rango que le dimos al usuario
		// de lo contrario nos pedira ingresar nuevamente el numero
		Mientras puntaje<4 o puntaje>20 Hacer
			// nos pide el ingreso infinitamente hasta que asignemos  valores entre 4 a 20
			Escribir 'puntaje no valido, Favor imgrese el puntaje del estudiante ',i,' El valor debe ser entre 4 a 20 puntos';
			Leer puntaje;
		FinMientras
		// Conversión del puntaje a nota
		Si puntaje>=18 Y puntaje<=20 Entonces
			Escribir 'El estudiante ',i,' obtuvo nota 7';
			nota_7 <- nota_7+1;
		SiNo
			Si puntaje>=15 Y puntaje<=17 Entonces
				Escribir 'El estudiante ',i,' obtuvo nota 6';
				nota_6 <- nota_6+1;
			SiNo
				Si puntaje>=12 Y puntaje<=14 Entonces
					Escribir 'El estudiante ',i,' obtuvo nota 5';
					nota_5 <- nota_5+1;
				SiNo
					Si puntaje>=9 Y puntaje<=11 Entonces
						Escribir 'El estudiante ',i,' obtuvo nota 4';
						nota_4 <- nota_4+1;
					SiNo
						// este numero salrá en caso de ser 4 a 8
						Escribir 'El estudiante ',i,' obtuvo nota 3';
					FinSi
				FinSi
			FinSi
		FinSi
	FinPara
	// Salida de resultados
	Escribir 'Cantidad de estudiantes con nota 4: ',nota_4;
	Escribir 'Cantidad de estudiantes con nota 5: ',nota_5;
	Escribir 'Cantidad de estudiantes con nota 6: ',nota_6;
	Escribir 'Cantidad de estudiantes con nota 7: ',nota_7;
FinProceso
