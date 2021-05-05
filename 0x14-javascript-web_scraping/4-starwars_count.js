#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const dict = JSON.parse(body);
    const movies = dict.results;
    for (let i = 0; i < movies.length; i++) {
      if (movies[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count += 1;
      }
    }
    console.log(count);
  }
});
