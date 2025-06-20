
let num = Number(prompt("შეიყვანეთ ციფრი:"));
let i = 0;
while (i <= num) {
    console.log(i);
    i++;
}


let name = prompt("შეიყვანეთ სახელი:");
while (name.length < 10) {
    name = prompt("სახელი უნდა იყოს მინიმუმ 10 სიმბოლო. სცადეთ თავიდან:");
}


let pin = prompt("შეიყვანეთ პინკოდი:");
while (pin !== "6446") {
    pin = prompt("პინკოდი არასწორია. სცადეთ თავიდან:");
}


let password = prompt("შეიყვანეთ პაროლი:");
while (password !== "ვანოჩკა") {
    password = prompt("პაროლი არასწორია. სცადეთ თავიდან:");
}