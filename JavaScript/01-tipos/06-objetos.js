let nombre = "Pablo";
let barrio = "camacol";
let edad = 21;

let personaje = {
    nombre: "Pablo",
    barrio: "camacol",
    edad: 22,
};

console.log(personaje);
console.log(personaje.nombre);
console.log(personaje.edad);
console.log(personaje.barrio);
console.log(personaje['nombre']);

personaje.edad = 22;

personaje['edad'] = 22;