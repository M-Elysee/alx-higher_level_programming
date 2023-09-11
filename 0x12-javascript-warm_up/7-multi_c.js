#!/usr/bin/node
/* a script that prints x times “C is fun” */

const x = parseInt(process.argv[2], 10);
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('c is fun');
  }
}
