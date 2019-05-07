#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Missing size');
} else if (Math.floor(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
