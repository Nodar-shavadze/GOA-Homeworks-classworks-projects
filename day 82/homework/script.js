
for (let i = 2; i <= 20; i += 2) {
    console.log(i);
}


let str = "Example";
for (let i = 0; i < str.length; i++) {
    console.log(str[i]);
}


let arr = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < arr.length; i++) {
    if (i % 2 === 0) {
        console.log(arr[i]);
    }
}


let num = 2;
while (num <= 50) {
    console.log(num);
    num += 2;
}


let n = 2;
while (n <= 80) {
    sum += n;
    n += 2;
}
console.log("Sum of even numbers from 1 to 80:", sum);
