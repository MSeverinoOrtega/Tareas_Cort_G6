/* //let array = [1,2,3];

let frutas = ["manzanas","peras","bananas"]; // primer elemento de la lista parte en 0



let elementosAlAzar = [2,true,"nombre",undefined,null];
elementosAlAzar[1];

let primeraFruta = frutas[0];
let segundaFruta = frutas[1];
let TerceraFruta = frutas[2];


let posicion = frutas.indexOf("bananas"); // impresion de la posicion de donde se encuentra un dato. 
console.log(posicion);

frutas.push("naranjas"); //.push Agrega un elemento nuevo a la lista 
console.log(frutas) ;
frutas.shift(); //elimnina el primer elemento de una lista
console.log("--------------------------------");
console.log(frutas);



//* Rellena un array con los números del 1 al 10. Muéstralo por la consola

for (let i = 1; i <= 10; i++) {
    console.log(i);
    
}


//* Let amigos = ["pedro","maria","Joan","pili"];1- queremos que escriba "mis amigos son maria y Joan.” con el siguiente array , haz que muestre la frase por consola.

let amigos= ["pedro", " maria", " Joan", " Pili"];
console.log(`Mis amigos son ${amigos[1]} y ${amigos[2]}`);


//* Deberás crear un array para guardar los nombres de los meses del año , empezando por 0 para enero . Para comprobar el funcionamiento pide al usuario un número entre 0 y 11 y devuelve el nombre del mes del año . Se supone que el dato tecleado estará entre 0 y 11 ejemplo : Si tecleo el número 4 me deberá decir que el mes es mayo.

const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];


function mesesAnio() {
    for (let i = 0; i < meses.length; i++) {
        let num = parseInt(prompt('Ingresa un numero'));

        switch (meses[num]){
            case 'Enero':
                console.log('El mes es Enero');
                break;
            case 'Febrero':
                console.log('El mes es Febrero');
                break;    
            case 'Marzo':
                console.log('El mes es Marzo');
                break;    
            case 'Abril':
                console.log('El mes es Abril');
                break;    
            case 'Mayo':
                console.log('El mes es Mayo');
                break;    
            case 'Junio':
                console.log('El mes es Junio');
                break;    
            case 'Julio':
                console.log('El mes es Julio');
                break;    
            case 'Agosto':
                console.log('El mes es Agosto');
                break;    
            case 'Septiembre':
                console.log('El mes es Septiembre');
                break;    
            case 'Octubre':
                console.log('El mes es Octubre');
                break;    
            case 'Noviembre':
                console.log('El mes es Noviembre');
                break;    
            case 'Diciembre':
                console.log('El mes es Diciembre');
                break;    
        }
    }
}
mesesAnio();


//* Diseña una función llamada sumaLista() capaz de sumar todos los números que forman el array que se le pase como argumento.ejemplo : Si ejecuto sumaLista([2,4,5,1,2]) deberá devolver como resultado 14
function sumarLista(...args) {
    let total = 0;
    const result = args.reduce( (total, args) => total += args);
    console.log(result);
}
sumarLista(1, 2, 3, 4, 5, 20); */