#!/usr/bin/node
// a class Square that defines a square and inherits
const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row = row + c;
        }
        console.log(row);
      }
    }
  }
};
