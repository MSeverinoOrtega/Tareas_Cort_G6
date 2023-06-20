Proceso sin_titulo
	Escribir "usted se encuentra trabajando";
	Leer Trabajandoo;
	Si Trabajandoo= "si" O Trabajandoo= "Si" Entonces
		Escribir "Que edad tiene";
		Leer Edad;
		Si Edad>45 Entonces
			Escribir "para calcular su bono indique su sueldo. Si su sueldo supera los $700.000, usted no recibira el bono";
			Leer sueldo;
			Si sueldo>=410000 y sueldo <=500000 Entonces
				monto1 <- (sueldo*0.2)+sueldo;
				Escribir "usted obtiene un bono de 2% ",sueldo*0.2;
				Escribir "el total a pago que recibira será de ", monto1;
			SiNo
				Si sueldo>500000 y sueldo<=700000 Entonces
					Escribir "usted obtiene un bono de 1,2% ",sueldo*0.12;
					monto1 <- (sueldo*0.12)+sueldo;
					Escribir "el total a pago que recibira será de ", monto1;
				SiNo
					Escribir "usted no recibe bono";
				FinSi
			FinSi
		SiNo
			Escribir "usted no es beneficiario del bono";
		FinSi
	SiNo
		Escribir "usted no es beneficiario";
	FinSi
FinProceso
