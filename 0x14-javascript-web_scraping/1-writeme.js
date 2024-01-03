#!/usr/bin/node
const fs = require('fs')

const filepath = process.argv[2];
const contentTowrite = process.argv[3];

fs.writeFile(filepath, contentTowrite, 'utf-8', (err) =>  {
    if (err) {
        console.error(err);
    }
});