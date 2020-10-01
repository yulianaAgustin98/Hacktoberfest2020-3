function decimalToBinary(n) {

    let binaryDigits = [];
    while (n > 0) {
        binaryDigits.unshift(n % 2);
        n = Math.floor(n / 2);
    }
    return binaryDigits.join("");
}