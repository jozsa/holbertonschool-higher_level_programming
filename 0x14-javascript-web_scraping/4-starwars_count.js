#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let info = JSON.parse(body).results;
    let count = 0;
    info.forEach(function (element) {
      if (element.characters.includes('https://swapi.co/api/people/18/')) { count++; }
    });
    console.log(count);
  }
});
