Proceso sin_titulo
	Escribir "favor ingrese la cantidad de dias del mes que desea ver";
	Leer n1;
	Si n1=31 Entonces
		Escribir "enero, marzo, mayo,julio,agosto,octubre y diciembre";
	SiNo
		Si n1=30 Entonces
			Escribir "abril, junio,septiembre,noviembre";
		SiNo
			Si n1= 29 o n1=28 Entonces
				Escribir "febrero";
			SiNo
				Escribir "ingrese dias validos para determinar un mes";
			FinSi
		FinSi
	FinSi
FinProceso
