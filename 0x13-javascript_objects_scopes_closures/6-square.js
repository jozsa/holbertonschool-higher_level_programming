#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let s = 0; s < this.width; s++) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
