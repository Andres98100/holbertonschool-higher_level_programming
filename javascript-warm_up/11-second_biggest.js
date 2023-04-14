#!/usr/bin/node

const process = require('process');
const args = process.argv;
let maxNumber = args[2];
let secNumber = args[2];
if (args.length > 2) {
  for (let index = 0; index < args.length; index++) {
    if (maxNumber < args[index]) {
      secNumber = maxNumber;
      maxNumber = args[index];
    } else if (args[index] > secNumber) {
      secNumber = args[index];
    }
  }
}
console.log(secNumber);
