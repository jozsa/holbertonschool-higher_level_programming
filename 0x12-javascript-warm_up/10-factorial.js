#!/usr/bin/node
function factorial (n = 1) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(process.argv[2]));
