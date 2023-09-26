#!/usr/bin/node
/* script that computes the number of tasks completed by user id */

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const count = {};

    for (const task of tasks) {
      if (task.completed) {
        if (count[task.userId]) {
          count[task.userId]++;
        } else {
          count[task.userId] = 1;
        }
      }
    }
    console.log(count);
  }
});
