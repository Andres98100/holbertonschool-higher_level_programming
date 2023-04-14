#!/usr/bin/node

function add (a, b) {
  const process = require('process');
  const args = process.argv;
  a = parseInt(args[2]);
  b = parseInt(args[3]);
  if (args.length > 2) {
    let add = 0;
    add = a + b;
    console.log(add);
  } else {
    console.log(NaN);
  }
}

add();
