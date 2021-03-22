#!/usr/bin/node
/*
Script that computes and prints a factorial
*/
const arg = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n) === true) {
    return 1;
  }
  if (n === 1) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(arg));
