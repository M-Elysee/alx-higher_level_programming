#!/usr/bin/node
// a function that returns the reversed version of a list
exports.esrever = function (list) {
  return list.reduceRight((arr, e) => { arr.push(e); return arr; }, []);
};
