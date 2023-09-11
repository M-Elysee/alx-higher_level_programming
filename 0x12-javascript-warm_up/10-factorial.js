#!/usr/bin/node
/* a script that computes and prints a factorial */

const num = parseInt(process.argv[2], 10);
function factorial (arg) {
  if (!arg || arg === 1) {
    return (1);
  }
  return (arg * factorial(arg - 1));
}
console.log(factorial(num));
