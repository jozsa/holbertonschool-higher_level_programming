#!/usr/bin/node
const mySquare = require('./5-square.js');
class Square extends mySquare {
  charPrint (c = 'X') {
    if (c === undefined) {
      c = 'X';
    }
    for (let s = 0; s < this.size; s++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
