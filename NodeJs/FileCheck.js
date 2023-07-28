var http = require('http');
//File system module
var fs = require('fs');
http.createServer(function (req, res) {
  //Reads the file and puts its output on screen
  fs.readFile('demofile1.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    res.end();
  });
}).listen(8080); 