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

    chars.forEach(function (charUrl) {
      request.get(charUrl, function (err2, resp2, charBody) {
        if (err2) {
          console.log(err);
        } else {
          const char = JSON.parse(charBody);
          console.log(char.name);
        }
      });
    });
  }
});
