Proceso sin_titulo
	Escribir "ingresa las 3 Calificaciones correspondientes del 1.0 al 7.0";
	Escribir "calificacion 1";
	Leer C1;
	Escribir "calificacion 2";
	Leer C2;
	Escribir "calificacion 3";
	Leer C3;
	Calificaciones <- (C1+C2+C3)/3;
	Si c1<7.1 y C2<7.1 y C3<7.1 Entonces
		Si Calificaciones >=4.0 y Calificaciones <=7.0 Entonces
			Escribir "su calificacion es ", Calificaciones, "  aprueba el curso";
		SiNo
			Escribir "reprueba";
		FinSi
	SiNo
		Escribir "ingrese calificaciones validas";
	FinSi
FinProceso
