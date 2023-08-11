const request = require('request');

function printMovieCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('API Error:', response.statusCode, body);
      return;
    }

    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    console.log(`Characters in "${movieData.title}":`);

    characters.forEach((characterUrl, index) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Character Error:', charError);
          return;
        }

        const characterData = JSON.parse(charBody);
        console.log(`${index + 1}. ${characterData.name}`);
        
        if (index === characters.length - 1) {
          console.log('All characters printed.');
        }
      });
    });
  });
}

// Get the movie ID from command line argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command line argument.');
} else {
  printMovieCharacters(movieId);
}
