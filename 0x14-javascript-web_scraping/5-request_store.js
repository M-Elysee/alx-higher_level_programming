#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.

const fs = require('fs');
const request = require('request');
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
