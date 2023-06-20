/* /Crea una función llamada numeroMayor() que toma tres números como entrada y retornar el número mayor de ellos, si son iguales, devolver un String «Los números son iguales»./

function numeroMayor(n1, n2, n3) {
    if (n1 > n2 && n1 > n3) {
        return n1
    } else if (n2 > n1 && n2 > n3) {
        return n2
    } else if (n3 > n1 && n3 > n2) {
        return n3
    } else {
        return "Los numeros son iguales"
    }
}

const respuesta = numeroMayor(4, 8, 7);
console.log(`El numero mayor es ${respuesta}`)

/Escriba una función con el nombre de esVocal() que tome un carácter, devuelva True si es vocal (no importa si es mayúscula o minúscula), y devuelva False en caso contrario/

const esVocal = (d) => {
    if (d === "a" || d === "e" || d === "i" || d === "o" || d === "u") {
        return true
    } else if (d === "A" || d === "E" || d === "I" || d === "O" || d === "U") {
        return true
    } else {
    return false;
    }
}

const respuesta2 = esVocal("u");
console.log(respuesta2);

/Crea una función llamada generar_caracteres() que tome como parámetro un número entero (n) y un carácter, retornar el carácter multiplicado por n. Por ejemplo, generar_caracteres(5,x), debería retornar “String” «xxxxx»./

const generar_caracteres = (numero, caracter) => {
    let responder = " "
    for (let i = 0; i < numero; i++) {
        responder += caracter;
    }
    return responder;
}
const respuesta3 = generar_caracteres(7, "b");
console.log(respuesta3)

/Crear una función sumaArreglo() que tome como parámetro un arreglo de números, retornar la longitud del arreglo + la suma de todos los números del arreglo/

function sumaArreglo(arreglo) {

    const longArreglo = arreglo.length;
    let sumaArreglo = 0;
    for (let i = 0; i < longArreglo; i++) {
        sumaArreglo += arreglo[i];
    }

    return sumaArreglo + longArreglo;

}

const respuesta4 = sumaArreglo([4, 7, 9, 1, 3]);
console.log(respuesta4)

/Crear una función multiplicarArreglo() que tome como parámetro un arreglo de números, retornar la multiplicación del número menor del arreglo y el número mayor del arreglo./

function multiplicarArreglo (arreglo1) {

    const minimo = Math.min(...arreglo1);
    const maximo = Math.max(...arreglo1);
    return minimo * maximo;
}

const respuesta5 = multiplicarArreglo([5, 7, 2, 9]);
console.log(respuesta5)

/Crear una función con el nombre de booleanoArray() que tome dos arreglos de números como parámetro y que retorne un booleano, unir los dos arreglos en uno solo, si la longitud del nuevo arreglo es mayor o igual a 10 que retorne true si es menor a 10 que retorne false./

function booleanoArray (array1, array2) {
    let = newArreglo = [...array1, ...array2];
    if(newArreglo.length >= 10) {
        return true;
    } else {
        return false
    }
}

const respuesta6 = booleanoArray([3, 2, 5, 7, 8, 9], [1, 6, 8, 4]);
console.log(respuesta6)

/Crear una función con el nombre de funcionArray() que tome dos arreglos de números enteros como parámetro y retornar un único arreglo, cada elemento del arreglo debe estar multiplicado por dos. ej: [2,5,2][1,5,3] -> [4,10,4,2,10,6]./

function funcionArray(arrays1, arrays2) {
    let arreglo2 = [...arrays1, ...arrays2];
    arreglo2 = arreglo2.map((elemento) => {
        return elemento *2
    });

    return arreglo2;
}

const respuesta7 = funcionArray([3, 4, 5], [1, 2, 3]);
console.log(respuesta7)  */