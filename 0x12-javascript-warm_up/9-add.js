#!/usr/bin/node
function add (a, b) {
  return Math.floor(a) + Math.floor(b);
}
console.log(add(process.argv[2], process.argv[3]));
