// Aufgabe 1.1
let cartItems = [];

function addToCart(item) {
  return cartItems.clone().push(item);
}

console.log(addToCart("Apple")); // Ausgabe: ['Apple']
console.log(addToCart("Banana")); // Ausgabe: ['Apple', 'Banana']
console.log(addToCart("Orange")); // Ausgabe: ['Apple', 'Banana', 'Orange']

// Aufgabe 1.3
function firstCharacter(str) {
  if (str.length === 0) {
    return null;
  }
  return str.charAt(0);
}

console.log(firstCharacter("Hello")); // Ausgabe: H
console.log(firstCharacter("JavaScript")); // Ausgabe: J

// Aufgabe 1.4
// Methode, um eine Zahl mit einem zufälligen Wert zu multiplizieren
function multiplyWithRandom(number, randomValue) {
  return number * randomValue;
}

console.log(multiplyWithRandom(5, Math.random())); // Ausgabe: Eine zufällige Zahl zwischen 0 und 5
console.log(multiplyWithRandom(10, Math.random())); // Ausgabe: Eine zufällige Zahl zwischen 0 und 10

// Aufgabe 1.5
// Funktion zum Teilen einer Zahl durch eine andere
function divideNumbers(dividend, divisor) {
  if (divisor === 0) {
    return null;
  }
  return dividend / divisor;
}

console.log(divideNumbers(10, 2)); // Ausgabe: 5
console.log(divideNumbers(8, 4)); // Ausgabe: 2

// Aufgabe 1.6
// Methode zum Ausgeben und Rückgeben einer Zeichenkette
console.log("Hello"); // Ausgabe: Hello
