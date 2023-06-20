Proceso a
	Escribir "seleccione un numero del 1 al 7 para elegir un dia de la semana";
	Leer N1;
	Si N1=1 Entonces
		Escribir "lunes";
	SiNo
		Si N1=2 Entonces
			Escribir "Martes";
		SiNo
			Si N1=3 Entonces
				Escribir "Miercoles";
			SiNo
				Si N1=4 Entonces
					Escribir "Jueves";
				SiNo
					Si N1=5 Entonces
						Escribir "viernes";
					SiNo
						Si N1=6 Entonces
							Escribir "Sabado";
						SiNo
							Si N1=7 Entonces
								Escribir "domingo";
							SiNo
								Escribir "ingrese un numero valido";
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
