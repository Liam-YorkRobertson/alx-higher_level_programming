#!/usr/bin/node
/* script that prints all characters of a Star Wars movie */

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    const chars = movie.characters;

    function printChars (chars) {
      if (chars.length === 0) {
        return;
      }

      const charUrl = chars.shift();
      request.get(charUrl, function (err2, resp2, body2) {
        if (err2) {
          console.log(err2);
        } else {
          const charData = JSON.parse(body2);
          console.log(charData.name);
          printChars(chars);
        }
      });
    }
    printChars(chars);
  }
});
