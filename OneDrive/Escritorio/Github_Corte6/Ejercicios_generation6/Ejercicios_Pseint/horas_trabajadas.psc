Proceso sin_titulo
	Escribir "ingrese las horas trabajadas";
	Leer n1;
	calculoa <- n1*1600;
	Si n1<=40 Entonces
		Escribir "su total a recibir es ", calculoa;
	SiNo
		Si n1>40 y n1<150 Entonces
			calculoss <- (n1-40)*2000;
			Escribir "su total a recibir es ", (40*1600)+calculoss;
		SiNo
			Escribir "ingrese horas validas por favor.";
		FinSi
	FinSi
FinProceso
