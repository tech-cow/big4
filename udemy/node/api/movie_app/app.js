var express = require("express");
var app = express();
var request = require("request")

/******* Configuration *******/
app.set("view engine","ejs");


app.get("/",function(req,res){
    res.send("Hello");
});

app.get("/results", function(req,res){
    request("http://www.omdbapi.com/?s=california", function(error,response,body){
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
