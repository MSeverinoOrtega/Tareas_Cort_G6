Proceso Suma_PosNeg
	// Declaración de variables
	// Inicialización de variables
	// la suma del postivo y negativo se hará abajo
	suma_pos <- 0;
	suma_neg <- 0;
	i <- 1;
	// Ciclo para ingresar los números
	// El <=10, indicará que son 10 vueltas
	Mientras i<=10 Hacer
		// Lectura del número
		Escribir 'Ingrese un número:';
		// el numero de lectura debe ir dentro del ciclo para que se cumpla
		Leer num;
		// Validación del número
		Mientras num=0 Hacer
			// Validamos que si el num es = 0 
			// se repita hasta que pongamos un numero negativo o positivo
			Escribir 'El número ingresado no puede ser cero. Ingrese otro número:';
			Leer num;
		FinMientras
		// Suma de los números positivos y negativos
		// Aquí hacemos la declaración V o F para acumular los postivos y negativos
		Si num>0 Entonces
			suma_pos <- suma_pos+num;
			// Aquí se acumularán la suma total de los positivos
		SiNo
			suma_neg <- suma_neg+num;
			// Aquí se acumularán la suma de los negativo
		FinSi
		// i<-i+1 indica es el indicador para que las vueltas vaya avanzando
		// empieza en 1 y con cada vuelta se va sumando a si mimso
		i <- i+1;
	FinMientras
	// Salida de resultados
	Escribir 'La suma de los números positivos es:',suma_pos;
	Escribir 'La suma de los números negativos es:',suma_neg;
FinProceso
