#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let characters = [];
const characterNames = [];

// Function to request and store character data
const requestAndStoreCharacters = async () => {
  try {
    // Fetch movie data
    const movieResponse = await fetchApiData(filmEndPoint);

    // Store characters' URLs
    characters = movieResponse.characters;
  } catch (error) {
    handleError(error, 'Fetching movie data');
  }
};

// Function to fetch data from the API
const fetchApiData = url => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error || new Error(`API Error: ${response.statusCode}`));
      } else {
        const jsonData = JSON.parse(body);
        resolve(jsonData);
      }
    });
  });
};

// Function to request and store character names
const requestAndStoreNames = async () => {
  if (characters.length > 0) {
    for (const characterUrl of characters) {
      try {
        // Fetch character data
        const characterResponse = await fetchApiData(characterUrl);

        // Store character name
        characterNames.push(characterResponse.name);
      } catch (error) {
        handleError(error, 'Fetching character data');
      }
    }
  } else {
    console.error('Error: Got no characters for some reason');
  }
};

// Function to handle errors
const handleError = (error, context) => {
  console.error(`Error (${context}):`, error.message);
};

// Function to display character names
const displayCharacterNames = () => {
  for (let i = 0; i < characterNames.length; i++) {
    if (i === characterNames.length - 1) {
      process.stdout.write(characterNames[i]);
    } else {
      process.stdout.write(characterNames[i] + '\n');
    }
  }
};

// Main function
const main = async () => {
  await requestAndStoreCharacters();
  await requestAndStoreNames();

  displayCharacterNames();
};

main();
