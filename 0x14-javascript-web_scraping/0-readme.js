#!/usr/bin/node
const filePath = process.argv[2];
const fs = require('fs');
fs.readFile(filePath, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
