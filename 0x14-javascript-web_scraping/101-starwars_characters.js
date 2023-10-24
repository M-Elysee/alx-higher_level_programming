#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

const movieId = process.argv[2];
request.get(url + movieId, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  function fetchCharacter (index) {
    if (index < characters.length) {
      request.get(characters[index], (e, r, b) => {
        if (e) {
          console.error(e);
        } else {
          console.log(JSON.parse(b).name);
        }
        fetchCharacter(index + 1);
      });
    }
  }
  fetchCharacter(0);
});
