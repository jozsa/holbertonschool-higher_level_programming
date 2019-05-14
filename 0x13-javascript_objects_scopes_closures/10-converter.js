#!/usr/bin/node
exports.converter = function (base) {
  return function () {
    return arguments[0].toString(base);
  };
};
