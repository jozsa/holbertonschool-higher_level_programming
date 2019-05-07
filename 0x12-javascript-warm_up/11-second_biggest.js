#!/usr/bin/node
let myNumberArray = [];
if (process.argv.length < 4) {
  console.log('0');
} else {
  for (let i = 2; i < process.argv.length; i++) {
    myNumberArray.push(process.argv[i]);
  }
  myNumberArray.sort(function (a, b) { return b - a; });
  console.log(myNumberArray[1]);
}
