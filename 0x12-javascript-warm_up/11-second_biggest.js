#!/usr/bin/node
/* a script that searches the second biggest integer in the list of arguments */

let i = 2;
let secBig = 0;
let big = 0;
while (parseInt(process.argv[i], 10)) {
  let arg = parseInt(process.argv[i]);
  if (arg > big) {
    secBig = big;
    big = arg;
  }
  i++;
}
console.log(secBig);
