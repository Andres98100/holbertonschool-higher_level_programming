#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.readPath(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
