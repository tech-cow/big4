var express = require("express");
var app = express();
var request = require("request")

/******* Configuration *******/
app.set("view engine","ejs");
app.use(express.static(__dirname + '/public'));


app.get("/",function(req,res){
  res.render("search");
});

// app.get("/search",function(req,res){
    // res.render("search");
// });

app.get("/results", function(req,res){
    var query = req.query.movieName;
    var url = "http://www.omdbapi.com/?s=" + query;

    request(url, function(error,response,body){
        if(!error && response.statusCode == 200){
          //body is an string, parsing turn string to an object
          var data = JSON.parse(body)
          res.render("results",{data,data})
        }
    })
});

app.listen(3000, function(){
    console.log("Server started!");
});
