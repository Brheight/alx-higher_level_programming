#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmsData = JSON.parse(body);
    const wedgeAntillesMovies = filmsData.results.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(wedgeAntillesMovies.length);
  } else {
    console.error(`Error: ${error}`);
  }
});
