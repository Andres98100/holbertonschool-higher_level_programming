#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 18;
request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(response.body).results;
    let count = 0;
    for (const film of data) {
      const characters = film.characters;
      for (const character of characters) {
        if (character.includes(`/${characterId}/`)) {
          count++;
          break;
        }
      }
    }
    console.log(`${count}`);
  }
});
