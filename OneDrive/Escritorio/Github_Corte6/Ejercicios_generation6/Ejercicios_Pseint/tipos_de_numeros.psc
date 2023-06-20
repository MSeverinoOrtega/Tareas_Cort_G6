Proceso sin_titulo
	Escribir "ingresa un numero ";
	Leer J1;
	Si J1= 1 Entonces
		Escribir "UNO";
	SiNo
		Si J1=2 Entonces
			Escribir "DOS";
		SiNo
			Si J1=3 Entonces
				Escribir "TRES";
			SiNo
				Si J1=0 Entonces
					Escribir " NUMERO QUE SE INGRESO ES NEUTRO";
				SiNo
					Si J1>3 Entonces
						Escribir "EL NUMERO QUE SE INGRESO ES MAYOR A 3";
					SiNo
						Escribir "EL NUMERO QUE SE INGRESO ES NEGATIVO";
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
