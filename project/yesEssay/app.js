// VARIABLE
var express     = require('express'),
    mongoose    = require('mongoose'),
    bodyParser  = require('body-parser'),
    methodOverride = require('method-override'),
    app         = express();

// APP CONFIG
// mongoose.connect('mongodb://localhost/yesessay');
app.set("view engine","ejs");
app.use(express.static(__dirname + "/public"));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(methodOverride('_method'));

/*********** RESTFUL ROUTES ***********/
app.get("/",function(req,res){
    res.redirect('/home');
});

// #1: INDEX ROUTE
app.get("/home",function(req,res){
    res.render('home');
});

//SERVER
app.listen(3000,function(){
    console.log("Server is connected");
});
