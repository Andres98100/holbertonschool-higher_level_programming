#!/usr/bin/node

const process = require('process');
const args = process.argv;
const n = parseInt(args[2]);
function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(n));
