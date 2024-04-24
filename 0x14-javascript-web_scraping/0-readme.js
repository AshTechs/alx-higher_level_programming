#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // 'utf8' specifies the encoding of the file being read

  if (error) {
    console.error('Error reading the file:', error);

  } else {
    console.log(content);
  }
});
