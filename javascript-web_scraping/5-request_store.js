#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, response.body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
