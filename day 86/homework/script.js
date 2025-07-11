
const arr = [];
for (let i = 1; i <= 30; i++) {
    arr.push(i);
}
for (const el of arr) {
    console.log(el);
}


const list1 = [];
const list2 = [];
for (let i = 1; i <= 10; i++) {
    list1.push(i);
}
for (const el of list1) {
    list2.push(el);
}
console.log(list2);


const str = "Hello World";
const vowels = "aeiouAEIOU";
for (const char of str) {
    if (vowels.includes(char)) {
        console.log(char);
    }
}

/*  
- block scope: ცვლადი ხელმისაწვდომია მხოლოდ ბლოკის ({}-ის) შიგნით (let, const).
- global scope: ცვლადი ხელმისაწვდომია მთელ სკრიპტში.
- local scope: ცვლადი ხელმისაწვდომია მხოლოდ ფუნქციის შიგნით.
*/

/* 5) მაგალითები */
let globalVar = "I am global"; // global scope

function myFunc() {
    let localVar = "I am local"; // local scope
    if (true) {
        let blockVar = "I am block scoped"; // block scope
        console.log(blockVar);
    }
    
    console.log(localVar);
}

myFunc();
console.log(globalVar);
