#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
let todoDict = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let info = JSON.parse(body);
    info.forEach(function (element) {
      if (element.completed) {
        if (element.userId in todoDict) {
          todoDict[element.userId] += 1;
        } else {
          todoDict[element.userId] = 1;
        }
      }
    });
  }
  console.log(todoDict);
});
