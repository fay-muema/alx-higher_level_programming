#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const nb = ++number;
  theFunction.call(this, nb);
};
