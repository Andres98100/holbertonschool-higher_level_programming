#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request.get(url, function (error, response) {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(response.body);
    console.log(`${movie.title}`);
  }
});
