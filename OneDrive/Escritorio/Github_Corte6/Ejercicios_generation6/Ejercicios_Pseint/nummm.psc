Proceso nummm
	suma_pos <- 0;
	suma_nev <- 0;
	i <- 1;
	Leer n;
	Mientras i<=10 Hacer
		Mientras n=0 Hacer
			Escribir "favor ingresar un num distinto a 0";
			Leer n;
		FinMientras
		Si n>0 Entonces
			suma_pos <- suma_pos+n;
		SiNo
			sumea_nev <- suma_nev+n;
		FinSi
		i <- i+1;
	FinMientras
FinProceso
