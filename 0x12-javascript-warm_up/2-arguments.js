#!/usr/bin/node
let process.argv.length = 3;
if (process.argv.length < 3){
	console.log( 'No argument' );
} else if (process.argv.length === 3){
	console.log( 'Argument found' );
} else {console.log( 'Arguments found' );}
