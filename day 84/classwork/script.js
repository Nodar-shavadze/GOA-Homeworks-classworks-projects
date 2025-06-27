function printNumbers(num) {
    for (let i = 1; i <= num; i++) {
        console.log(i);
    }
}

function greetUser(name, age) {
    if (age < 18) {
        return "your not adult yet";
    } else {
        return `Hello, ${name}!`;
    }
}

function printNameLetters(name) {
    for (let i = 0; i < name.length; i++) {
        console.log(name[i]);
    }
}