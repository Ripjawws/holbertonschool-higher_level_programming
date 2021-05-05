#!/usr/bin/node
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', function (err, result) {
      if (err) {
        console.log(err);
      }
    });
  }
});
