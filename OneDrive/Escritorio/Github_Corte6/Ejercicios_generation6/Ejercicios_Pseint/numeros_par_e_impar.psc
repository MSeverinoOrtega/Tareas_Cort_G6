Proceso sin_titulo
	Escribir " ingresa 2 numeros ";
	Leer n1;
	n11 <- n1 % 2;
	Leer n2;
	n22 <- n2 % 2;
	Si n11=0 y n22=0 Entonces
		Escribir "favor ingresar numeros diferentes, no 2 pares";
	SiNo
		Si n11=1 y n22=1 Entonces
			Escribir "favor ingresar numeros diferentes, no 2 impares";
		SiNo
			Si n11=0 y n22=1 Entonces
				Escribir "el producto de los 2 numeros es ", n1*n2;
			SiNo
				Escribir "la division entre ellos es ", n1/n2;
			FinSi
		FinSi
	FinSi
FinProceso
