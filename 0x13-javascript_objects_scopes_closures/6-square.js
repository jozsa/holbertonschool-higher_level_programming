#!/usr/bin/node
'use strict';
const mySquare = require('./5-square.js');
class Square extends mySquare {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let s = 0; s < this.size; s++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
