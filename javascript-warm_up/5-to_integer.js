#!/usr/bin/node

const process = require('process');
const args = process.argv;
if (args.length >= 2) {
  const num = parseInt(args[2]);
  if (!isNaN(num)) {
    console.log('My number: ' + num);
  } else {
    console.log('Not a number');
  }
}
