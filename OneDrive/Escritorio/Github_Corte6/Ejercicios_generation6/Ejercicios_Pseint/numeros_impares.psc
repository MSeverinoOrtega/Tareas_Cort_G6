Proceso sin_titulo
	Escribir 'ingresar un numero en el rango de 10 a 86';
	Leer n1;
	Si n1>10 Y n1<86 Entonces
		Escribir 'Rango valido';
		n2 <- n1 % 2;
		Si n1=0 Entonces
			Escribir 'par';
		SiNo
			Escribir 'impar';
		FinSi
	SiNo
		Escribir 'fuera de rango';
	FinSi
FinProceso
