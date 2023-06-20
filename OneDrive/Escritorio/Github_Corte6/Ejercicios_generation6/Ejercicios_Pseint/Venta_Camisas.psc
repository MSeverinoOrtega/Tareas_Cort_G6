Proceso Venta_Camisas
	Escribir "Ingrese la cantidad de camisas que desea llevar";
	Leer N1;
	Escribir "Ingrese el precio de la camisa que desea llevar";
	Leer N2;
	Si N1>=3 Entonces
		Calulo <- N1*N2;
		Escribir "su total es de ", Calulo;
		Escribir "se le aplicara un decuento de 10%";
		cala <- (-Calulo*0.10)+Calulo;
		Escribir " El total a pagar es de ",cala;
	SiNo
		Calulo <- N1*N2;
		Escribir "su total es de ", calulo;
		Escribir "se le aplicara un descuento de 5%";
		calaw <- (-Calulo*0.05)+calulo;
		Escribir "El total a pagar es de ", calaw;
	FinSi
FinProceso
