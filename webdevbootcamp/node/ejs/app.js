var express = require("express");
var app = express();


// Including css
app.use(express.static(__dirname + '/public'));

//set the default file to be ejs
app.set("view engine","ejs");


//render
app.get("/", function(req, res) {
    res.render("home");
});

app.get("/fallinlovewith/:thing", function(req, res) {
    var thing = req.params.thing;
    res.render("love", {
        thingVar: thing
    });
});


app.get("/posts", function(req, res){
    var posts = [
      {title: "1", author: "yz"},
      {title: "2", author: "ms"},
      {title: "3", author: "bd"}
    ];
    res.render("posts",{posts: posts});
});



app.listen(3000, function() {
    console.log("Server is listening!");
});
