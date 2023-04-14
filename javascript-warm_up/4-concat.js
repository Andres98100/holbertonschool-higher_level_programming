#!/usr/bin/node

const process = require('process');
const args = process.argv;
if (args.length >= 2) {
  console.log(`${args[2]} is ${args[3]}`);
}
