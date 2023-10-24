#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require('request');
let count = 0;
const dic = {};
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    for (let i = 1; i <= 10; i++) {
      for (const obj of body) {
        if (obj.userId === i && obj.completed) {
          count++;
        }
      }
      dic[i] = count;
      count = 0;
    }
    console.log(dic);
  }
});
