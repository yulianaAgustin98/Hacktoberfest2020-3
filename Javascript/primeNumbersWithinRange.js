function primeNumbersWithinRange(number) {
  let result = [];

  for (let i = 2; i <= number; i++) {
    if (isPrime(i)) result.push(i);
  }

  return result;
}

function isPrime(number) {
  let result = true;

  for (let i = 2; i <= Math.floor(Math.sqrt(number)); i++) {
    if (number % i == 0) {
      result = false;
      break;
    }
  }
  return result;
}
