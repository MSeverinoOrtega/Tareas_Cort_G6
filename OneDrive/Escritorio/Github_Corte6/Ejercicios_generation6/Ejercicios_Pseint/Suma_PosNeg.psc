Proceso Suma_PosNeg
	// Declaraci�n de variables
	// Inicializaci�n de variables
	// la suma del postivo y negativo se har� abajo
	suma_pos <- 0;
	suma_neg <- 0;
	i <- 1;
	// Ciclo para ingresar los n�meros
	// El <=10, indicar� que son 10 vueltas
	Mientras i<=10 Hacer
		// Lectura del n�mero
		Escribir 'Ingrese un n�mero:';
		// el numero de lectura debe ir dentro del ciclo para que se cumpla
		Leer num;
		// Validaci�n del n�mero
		Mientras num=0 Hacer
			// Validamos que si el num es = 0 
			// se repita hasta que pongamos un numero negativo o positivo
			Escribir 'El n�mero ingresado no puede ser cero. Ingrese otro n�mero:';
			Leer num;
		FinMientras
		// Suma de los n�meros positivos y negativos
		// Aqu� hacemos la declaraci�n V o F para acumular los postivos y negativos
		Si num>0 Entonces
			suma_pos <- suma_pos+num;
			// Aqu� se acumular�n la suma total de los positivos
		SiNo
			suma_neg <- suma_neg+num;
			// Aqu� se acumular�n la suma de los negativo
		FinSi
		// i<-i+1 indica es el indicador para que las vueltas vaya avanzando
		// empieza en 1 y con cada vuelta se va sumando a si mimso
		i <- i+1;
	FinMientras
	// Salida de resultados
	Escribir 'La suma de los n�meros positivos es:',suma_pos;
	Escribir 'La suma de los n�meros negativos es:',suma_neg;
FinProceso
