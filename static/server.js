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

app.get('/index.html', function(request, response) {
	response.sendFile(__dirname + '/index.html');
});

app.get('/api/user', function(request, response) {
  response.redirect(301, 'https://127.0.0.1:8000/api/user');
});

app.get('*', function(request, response) {
	// response.status(404).body('404 not found');
	response.send('Not Found',404);
});

// app.post('/api/user', function(req, res) {
//   res.redirect(301, 'https://127.0.0.1:8000/api/user');
// });



app.listen(3000,function() {
	console.log('Listening at http://127.0.0.1:3000');
})
