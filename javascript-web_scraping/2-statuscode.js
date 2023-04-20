#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request.get(URL, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
