Proceso quehace
	a1 <- 0;
	a2 <- 0;
	con1 <- 0;
	con2 <- 0;
	Leer num;
	Para x<-1 Hasta 5 Hacer
		Si num>10 Entonces
			a1 <- a1+num;
			con1 <- con1+1;
		FinSi
		Si num<8 Entonces
			a2 <- a2+num;
			con2 <- con2+1;
		FinSi
	FinPara
	Si con1>0 Entonces
		Escribir 'promedio de los numeros mayores 10, es de :',a1/con1;
	FinSi
	Si con2>0 Entonces
		Escribir ' promedio de los numeros menores que 8, esde : ',a2/con2;
	FinSi
FinProceso
