#!/usr/bin/node
// a function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((i, e) => e === searchElement ? i + 1 : i, 0);
};
