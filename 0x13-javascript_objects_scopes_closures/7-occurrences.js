#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let count = 0;
	list.reduce((accumalator, currentElement) => {
		if (currentElement === searchElement) {
			count++;
		}
	}, 0);
	return count;
};
