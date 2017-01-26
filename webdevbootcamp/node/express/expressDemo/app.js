var express = require("express");
var app = express();


// root path:  "/" => "Hi there!"
app.get("/", function(req,res){
  // console.log("request to domain");
  res.send("Welcome to the werewolves world");
});

// "/bye" => "Googlebye!"

app.get("/r/:role",function(req,res){
  var role = req.params.role;
  res.send(role.toUpperCase() + " Rules");
});

app.get("*",function(req,res){
  res.send("YOLO");
});

app.listen(3000, function(){
  console.log("Server has started!!");
});
