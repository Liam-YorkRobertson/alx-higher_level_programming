#!/usr/bin/node
const argc = process.argv[2];
if (argc) {
  console.log(argc);
} else {
  console.log('No argument');
}
