Proceso sin_titulo
	Escribir "ingrese 3 cifras distintas";
	Leer N1;
	Leer N2;
	Leer N3;
	Si N1=N2 O N1=N3 o N2=N3 Entonces
		Escribir "Favor ingrese numeros que no se repitan entre sí";
	SiNo
		Si N1<N2 Y N1<N3 Y N2<N3 Entonces
			Escribir N1,N2,N3;
		SiNo
			Si N1<N2 Y N2>N3 Y N1<N3 Entonces
				Escribir N1,N3,N2;
			SiNo
				Si N2<N1 Y N2<N3 Y N1<N3 Entonces
					Escribir N2,N1,N3;
				SiNo
					Si N2<N1 Y N1>N3 Y N2<N3 Entonces
						Escribir N2,N3,N1;
					SiNo
						Si N3<N1 Y N3<N2 Y N2<N1 Entonces
							Escribir N3,N2,N1;
						SiNo
							Escribir N3,N1,N2;
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
