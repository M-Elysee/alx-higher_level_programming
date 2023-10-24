#!/usr/bin/node
//  a script that prints the number of movies where the character
// “Wedge Antilles” is present.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/';
let i = 0;
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const json = JSON.parse(body);
    for (const result of json.results) {
      for (const character of result.characters) {
        if (character === url + 'people/18/') {
          i++;
        }
      }
    }
    console.log(i);
  }
});
