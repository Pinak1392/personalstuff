var http = require('http');
var formidable = require('formidable');
var nodemailer = require('nodemailer');


http.createServer(function (req, res) {
  //Will upload requested file to the path u asked it to put it on
  if (req.url == '/email') {
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
      var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
          user: String(fields["Email"]),
          pass: String(fields["Pass"])
        }
      });
      
      var mailOptions = {
        from: String(fields["Email"]),
        to: String(fields["Receiver"]),
        subject: String(fields["Subject"]),
        text: String(fields["Msg"])
      };
      
      transporter.sendMail(mailOptions, function(error, info){
        if (error) {
          console.log(error);
        } else {
          console.log('Email sent: ' + info.response);
        }
      });
    });
  } else {
    //Creates a form for selecting a file
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<form action="email" method="post" enctype="multipart/form-data">');
    res.write('<h2>Email</h2>');
    res.write('<input type="text" name="Email"><br>');
    res.write('<h2>Password</h2>');
    res.write('<input type="password" name="Pass"><br>');
    res.write('<h2>Recipient</h2>');
    res.write('<input type="text" name="Receiver"><br>');
    res.write('<h2>Subject</h2>');
    res.write('<input type="text" name="Subject"><br>');
    res.write('<h2>Message</h2>');
    res.write('<input type="text" name="Msg"><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    return res.end();
  }
}).listen(8080); 
