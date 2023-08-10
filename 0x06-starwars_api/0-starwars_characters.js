#!/usr/bin/node

const request = require('request');
// getting the film value from the terminal
const os = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${os}`;

request(url, (err, res) => {
  if (err) {
    console.log(err);
  }
  const character = JSON.parse(res.body).characters;

  for (let i = 0; i < character.length; i++) {
    request(character[i], (err, res) => {
      if (err) {
        console.log(err);
      }

      const chars = JSON.parse(res.body);
      console.log(chars.name);
    });
  }
});
