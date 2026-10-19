#!/usr/bin/node
const first = process.argv[2];

console.log(first === undefined ? 'No argument' : first);
