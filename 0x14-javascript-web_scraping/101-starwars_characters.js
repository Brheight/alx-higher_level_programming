#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    function fetchCharacter(index) {
      if (index < charactersUrls.length) {
        const characterUrl = charactersUrls[index];
        request(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
            fetchCharacter(index + 1);
          } else {
            console.error(`Error: ${charError}`);
          }
        });
      }
    }

    fetchCharacter(0);
  } else {
    console.error(`Error: ${error}`);
  }
});
