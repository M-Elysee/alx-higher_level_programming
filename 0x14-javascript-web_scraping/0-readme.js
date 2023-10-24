#!/usr/bin/node
//  a script that reads and prints the content of a file.
const arg = process.argv[2];
const fs = require('fs');
fs.readFile(arg, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
