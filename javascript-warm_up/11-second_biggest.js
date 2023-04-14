#!/usr/bin/node

const process = require('process');
const args = process.argv;
let maxNumber = args[2];
let secNumber = args[2];

if (args.length > 2) {
  for (let index = 0; index < args.length - 2; index++) {
    let n = parseInt(args[index]);
    if (maxNumber < n) {
      secNumber = maxNumber;
      maxNumber = n;
    } else if (n > secNumber) {
      secNumber = n;
    }
  }
}
console.log(secNumber);
