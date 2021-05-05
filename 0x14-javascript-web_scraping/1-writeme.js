#!/usr/bin/node
const filePath = process.argv[2];
const stringToAdd = process.argv[3];
const fs = require('fs');
fs.writeFile(filePath, stringToAdd, 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
