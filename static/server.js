var express = require('express');
var app = express();

// var mode   = process.env.NODE_ENV;
// const hostname = process.env.HOST;
// const port = process.env.PORT;

// console.log()

app.use('/static/',express.static(__dirname + '/'));

app.get('/', function(request, response) {
	response.sendFile(__dirname + '/index.html');
});

app.get('*', function(request, response) {
	response.send('Not Found',404);
});

app.listen(3000,function() {
	console.log('Listening at http://127.0.0.1:3000');
})
