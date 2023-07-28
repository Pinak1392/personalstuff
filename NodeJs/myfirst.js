//Gives access to the http and url module of node
var http = require('http');
var url = require('url');
//Gets modules from newModule file which i created
var dt = require('./newModule');

//Returns hello world when u connect to port 8080 on localhost(your computer)
http.createServer(function (req, res) {
    //Writes the next write as a html text
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write("The date and time is currently: " + dt.myDateTime());

    //The bottom part writes out the /url after the main part
    res.write(" " + req.url);

    //Url gets the variables u get after the ? in the url
    var q = url.parse(req.url, true).query;
    var txt = " " + q.year + " " + q.month;
    res.end(txt);
}).listen(8080); 