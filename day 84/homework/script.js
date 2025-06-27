
function greetNTimes(number) {
    let i = 0;
    while (i < number) {
        console.log("მოგესალმებით!");
        i++;
    }
}

let num = 7; 
let guess;

do {
    guess = Number(prompt("შეიყვანეთ რიცხვი 1-დან 10-მდე:"));
    switch (guess) {
        case num:
            alert("გილოცავთ, სწორად გამოიცანით!");
            break;
        default:
            alert("არასწორია, სცადეთ კიდევ ერთხელ!");
    }
} while (guess !== num);


function discountByAge(age) {
    if (age <= 19) {
        console.log("თქვენ მიიღეთ 30% ფასდაკლება");
    } else if (age >= 19 && age < 50) {
        console.log("თქვენ მიიღეთ 10% ფასდაკლება");
    } else if (age >= 50) {
        console.log("თქვენ მიიღეთ 50% ფასდაკლება");
    }
}

