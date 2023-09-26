#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles” is present */

const request = require('request');
const url = process.argv[2];
const id = 18;

request.get(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const hasWedgeAntilles = data.results.filter(function (film) {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`);
    });
    console.log(hasWedgeAntilles.length.toString());
  }
});
