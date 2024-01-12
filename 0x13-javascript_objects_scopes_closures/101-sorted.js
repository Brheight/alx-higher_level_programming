#!/usr/bin/node

const { dict } = require('./101-data');

const sortedDict = {};
Object.entries(dict).forEach(([userId, occurrences]) => {
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }
  sortedDict[occurrences].push(userId.toString());
});

console.log(sortedDict);
