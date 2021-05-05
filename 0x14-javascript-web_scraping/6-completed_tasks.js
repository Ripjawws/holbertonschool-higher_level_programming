#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    for (let i = 0; i < tasks.length; i++) {
      const key = tasks[i].userId;
      if (tasks[i].completed) {
        if (!(key in dict)) {
          dict[key] = 1;
        } else {
          dict[key] += 1;
        }
      }
    }
  }
  console.log(dict);
});
