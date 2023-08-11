#!/usr/bin/node

const request = require('request');

// Function to fetch movie data
const fetchMovieData = movieId => {
  const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

  return new Promise((resolve, reject) => {
    request(apiUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`API Error: ${response.statusCode}`));
      } else {
        const movieData = JSON.parse(body);
        resolve(movieData);
      }
    });
  });
};

// Function to fetch character data for a movie
const fetchCharacterData = characterUrl => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Character Error: ${response.statusCode}`));
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData);
      }
    });
  });
};

// Main function to print characters' names
const printMovieCharacters = async movieId => {
  try {
    const movieData = await fetchMovieData(movieId);
    const characters = movieData.characters;

    console.log(`Characters in "${movieData.title}":`);

    for (let index = 0; index < characters.length; index++) {
      const characterData = await fetchCharacterData(characters[index]);
      console.log(`${index + 1}. ${characterData.name}`);
    }

    console.log('All characters printed.');
  } catch (error) {
    console.error('Error:', error);
  }
};

// Get the movie ID from command line argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
} else {
  printMovieCharacters(movieId);
}

