var express = require("express");
var app = express();

//render
app.get("/",function(req,res){
  res.render("home.ejs");
});

app.get("/fallinlovewith/:thing",function(req,res){
  var thing = req.params.thing;
  res.render("love.ejs",{thingVar: thing});
});


// Including css
app.use(express.static(__dirname + '/public'));


app.listen(3000, function(){
  console.log("Server is listening!");
});
