var express    = require("express"),
    app        = express(),
    bodyParser = require("body-parser"),
    mongoose   = require("mongoose"),
    Campground = require("./models/campground"),
    seedDB     = require("./seed");

mongoose.connect("mongodb://localhost/yelp_camp");
app.use(bodyParser.urlencoded({ extended: true  }));
app.set("view engine","ejs");
seedDB();


//RESTFUL ROUTE
app.get("/",function(req,res){
    res.render("home");
});

//
app.get("/campgrounds",function(req,res){
    //Get all campgrounds from DB
    Campground.find({},function(err,allCampgrounds){
        if (err) {
            console.log(err);
        } else {
            res.render("index",{campgrounds:allCampgrounds});
        }
    });
    // res.render("campgrounds",{campgrounds,campgrounds})
});

app.post("/campgrounds",function(req,res){
    var name = req.body.name;
    var image = req.body.image;
    var desc = req.body.description;
    var newCampground = {name: name, image: image, description: desc};

    // Create new campgrounds and save to database
    Campground.create(newCampground, function(err,newly_created){
        if (err) {
            console.log(err);
        } else {
            console.log("Added ");
            res.redirect("/campgrounds");
        }
    });
  });

app.get("/campgrounds/new", function(req,res){
    res.render("new");
});


//SHOW   ...
app.get("/campgrounds/:id", function(req,res){
  // res.send("THIS WILL BE SHOWING PAGE ONE DAY");
    Campground.findById(req.params.id).populate("comments").exec(function(err, foundCampground){
        if (err) {
            console.log(err);
        } else {
            console.log(foundCampground);
            res.render("show",{campground: foundCampground});
        }
    });
});



app.listen(3000, function(){
    console.log("Server connected!");
});
