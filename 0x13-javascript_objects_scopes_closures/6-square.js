#!/usr/bin/node
const mySquare = require('./5-square.js');
class Square extends mySquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let s = 0; s < this.height; s++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
