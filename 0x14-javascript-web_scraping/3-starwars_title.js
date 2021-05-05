#!/usr/bin/node
const movieId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const fullURL = url.concat(movieId);
request(fullURL, function (error, request, body) {
  if (error) {
    console.error(error);
  } else {
    const dict = JSON.parse(body);
    console.log(dict.title);
  }
});
