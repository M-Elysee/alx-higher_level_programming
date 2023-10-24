#!/usr/bin/node
// a script that prints the title of a Star Wars movie where
// the episode number matches a given integer

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url + process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
