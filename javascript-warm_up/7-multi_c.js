#!/usr/bin/node

const process = require('process');
const args = process.argv;
const myString = 'C is fun';
if (args.length >= 2) {
  for (let i = 0; i < args[2]; i++) {
    console.log(myString);
  }
}
