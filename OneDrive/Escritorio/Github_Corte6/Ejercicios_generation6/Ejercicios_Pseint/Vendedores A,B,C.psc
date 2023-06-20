Proceso sin_titulo
	definir ventana1,ventana2,ventana3,ventasA,ventasB,ventasC como real;
	Escribir "ingrese ventas del vendedor A";
	Leer 	ventana1;
	ventasA <- ventana1*0.013;
	Escribir "Ingrese ventas del vendedor B";
	Leer ventana2;
	ventasB <- ventana2*0.012;
	Escribir "ingrese ventas del vendedor C";
	Leer Ventana3;
	ventasC <- ventana3*0.0123;
	Si ventasA>ventasB Y ventasA>ventasC Entonces
		mayorcomision <- ventasA;
		Escribir "El vendedor A obtuvo la mayor comision, por un monto de $", mayorcomision;
	SiNo
		Si ventasB>ventasC Y ventasB>ventasA Entonces
			mayorcomision <- ventasB;
			Escribir "El vendedor B obstuvo la mayor comision, por un monto de $", mayorcomision;
		SiNo
			mayorcomision <- ventasC;
			Escribir "El vendedor C obtuvo la mayor comision, por un monto de $", mayorcomision;
		FinSi
	FinSi
	Escribir "El vendedor A recibira ", ventasA+ventana1, " de dinero a pagar";
	Escribir "El vendedor B recibira ", ventasB+ventana2," de dinero a pagar";
	Escribir "El vendedor C recibira ", ventasC+ventana3, " de dinero a pagar";
FinProceso
