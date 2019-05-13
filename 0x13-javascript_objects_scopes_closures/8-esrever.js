#!/usr/bin/node
exports.esrever = function (list) {
  let newList = [];
  let len = list.length;
  for (let i = 0; i < len; i++) {
    let end = list.pop();
    newList.push(end);
  }
  return newList;
};
