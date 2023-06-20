// recibir un valor 

// compara ese valor con 7 y 8 verificando si es divisible entre ellos

// valor divisible entre 7
// valor divisible entre 8

// Si es verdadero ==> console.log( "Verdadero");
// caso contrario console.log( "Falso");
// 56 7 8 0 224 73





function valorRecibido(valor1){
    if (valor1 % 7 === 0 && valor1 % 8 === 0){
        console.log("Verdadero");
}
    else {
        console.log("falso");
}
}

valorRecibido(56)
valorRecibido(7)
valorRecibido(8)
valorRecibido(0)
valorRecibido(224)
valorRecibido(73)
