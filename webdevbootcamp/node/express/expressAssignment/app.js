var express = require('express')
var app = express()

// respond with "hello world" when a GET request is made to the homepage
app.get('/', function (req, res) {
  res.send('Hi there, welcome to my assignment!');
  console.log(req);

});

app.get('/speak/:animal',function(req,res){
  var sounds = {
    pig: "Oink",
    cow: "Moo!",
    dog: "Woof Woof!"
  }
  var animal = req.params.animal;
  var sound = sounds[animal];
  res.send ("the "+ animal + " says " + sound);
});


app.get('/repeat/:text/:num',function(req,res){
  var text = req.params.text;
  var num = req.params.num;
  var num_string = "";
  for (var i = 0; i < num; i++) {
    num_string += text + " ";
  }
  res.send(num_string);
});

app.get("*",function(req,res){
  res.send("What are you doing with your life?")
});



app.listen(3000,function(){
  console.log("The server succesfully operates");
});
