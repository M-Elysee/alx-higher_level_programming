#!/usr/bin/node
/* a script that prints a square */

const size = parseInt(process.argv[2], 10);
if (!size) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
