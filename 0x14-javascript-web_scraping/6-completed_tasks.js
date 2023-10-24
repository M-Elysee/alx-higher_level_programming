#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require('request');
let count;
const dic = {};
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    for (let i = 1; i <= 10; i++) {
      count = 0;
      for (const obj of body) {
        if (obj.userId === i && obj.completed) {
          count++;
        }
      }
      dic[i] = count;
    }
    console.log(dic);
  }
});
