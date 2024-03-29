#!/usr/bin/node
/* script that prints the title of a Star Wars movie where the episode number matches a given integer */

const request = require('request');
const episodeNum = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episodeNum}`;

request.get(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
