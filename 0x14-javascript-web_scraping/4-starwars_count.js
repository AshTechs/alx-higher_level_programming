#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
