#!/usr/bin/node

const process = require('process');
const args = process.argv;
let count = 0;
for (count in args) {
  count++;
}

if (count >= 3) {
  console.log(`${args[2]}`);
} else {
  console.log('No argument');
}
