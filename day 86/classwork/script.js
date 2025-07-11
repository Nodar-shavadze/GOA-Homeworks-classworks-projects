
const list = [10, 20, 30, 40, 50];
for (const item of list) {
    console.log(item);
}


const str = "GOA";
for (const char of str) {
    console.log(char);
}


const obj = {name: "Nodo", age: "12", city: "Batumi"};
for (const key in obj) {
    console.log(key, obj[key]);
}

/* 

Block scope: ცვლადი გამოყენებულია {} ბლოკის შიგნით (მაგ: if, for, function), let ან const-ით. ხელმისაწვდომია მხოლოდ ამ ბლოკში.
Local scope: ცვლადი გამოყენებულია ფუნქციის შიგნით. ხელმისაწვდომია მხოლოდ ამ ფუნქციაში.
Global scope: ცვლადი გამოყენებულია ყველა ბლოკის და ფუნქციის გარეთ. ხელმისაწვდომია ყველგან.
*/