
let age = 15;
if (age < 13) {
    console.log("You are kid");
} else if (age < 18) {
    console.log("You are not adult yet");
} else {
    console.log("You are adult");
}


let number = 7;
if (number % 2 === 0) {
    console.log(number);
} else {
    console.log("ეს რიცხვი კენტია");
}


//  Python-ში:
//  age = 15
//   if age < 13:
//      print("You are kid")
//  elif age < 18:
//      print("You are not adult yet")
//  else:
//      print("You are adult")

//  განსხვავებები:
//  - Python-ში ბლოკები განისაზღვრება ინდენტაციით, JS-ში {} ფრჩხილებით.
//  - Python-ში else if არის elif, JS-ში else if.


// "!" მოცემულ არგუმენტის პირიქით გამოტანის, მატალითად true-ს false-ად ან პირიქით.

let num = 27;
if (num % 3 === 0 && num % 9 === 0) {
    console.log(num);
} else {
    console.log("task was not completed.");
}