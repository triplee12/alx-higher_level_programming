#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/';
const movieId = process.argv[2];
request(apiUrl + movieId, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    console.log(characters)
  }
});
