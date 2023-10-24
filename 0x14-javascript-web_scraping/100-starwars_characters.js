#!/usr/bin/node
// a script that prints all characters of a Star Wars movie:
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    for (const character of JSON.parse(body).characters) {
      request.get(character, (e, r, b) => {
        if (e) {
          console.error(e);
        } else {
          console.log(JSON.parse(b).name);
        }
      });
    }
  }
});
