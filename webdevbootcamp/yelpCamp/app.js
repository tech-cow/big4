/*===================
   VARIABLES
====================*/
var express = require("express"),
    app = express(),
    bodyParser = require("body-parser"),
    mongoose = require("mongoose"),
    Campground = require("./models/campground"),
    Comment = require("./models/comment"),
    seedDB = require("./seed");


/*===================
   APP CONFIG
====================*/

mongoose.connect("mongodb://localhost/yelp_camp");
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + '/public'));
seedDB();

/*===================
   CAMPGROUNDS ROUTE
====================*/

app.get("/", function(req, res) {
    res.redirect("/campgrounds");
});

/* 1. INDEX ROUTE */
app.get("/campgrounds", function(req, res) {
    //Get all campgrounds from DB
    Campground.find({}, function(err, allCampgrounds) {
        if (err) {
            console.log(err);
        } else {
            res.render("campgrounds/index", {campgrounds: allCampgrounds});
        }
    });
});

/* 2. NEW ROUTE */
app.get("/campgrounds/new", function(req, res) {
    res.render("campgrounds/new");
});

/* 3. CREATE ROUTE */
app.post("/campgrounds", function(req, res) {
    var name  =  req.body.name,
        image =  req.body.image,
        desc  =  req.body.description;

    var newCampground = {
        name: name,
        image: image,
        description: desc
    };

    // Create new campgrounds and save to database
    Campground.create(newCampground, function(err, newly_created) {
        if (err) {
            console.log(err);
        } else {
            console.log("Added ");
            res.redirect("/campgrounds");
        }
    });
});


/* 4. SHOW ROUTE */
app.get("/campgrounds/:id", function(req, res) {
  Campground.findById(req.params.id).populate("comments").exec(function(err, foundCampground) {
        if (err) {
            console.log(err);
        } else {
            console.log(foundCampground);
            res.render("campgrounds/show", {campground: foundCampground});
        }
    });
});
/* 5. EDIT ROUTE */
/* 6. UPDATE ROUTE */
/* 7. DESTROY ROUTE */

/*===================
   COMMENTS ROUTE
====================*/

/* 1. NEW ROUTE */
app.get("/campgrounds/:id/comments/new", function(req,res){
    //find campgrounds by id
    Campground.findById(req.params.id, function(err,campground){
        if (err) {
            console.log(err);
        } else {
            res.render("comments/new", {campground: campground});
        }
    });
});

/* 2. CREATE ROUTE */
app.post("/campgrounds/:id/comments", function(req,res){
    //look up campground using id
    Campground.findById(req.params.id, function(err, campground){
        if (err) {
            console.log(err);
            res.redirect("/campgrounds");
        } else {
          Comment.create(req.body.comment, function(err, comment){
              if (err) {
                  console.log(err);
              } else {
                  campground.comments.push(comment);
                  campground.save();
                  res.redirect('/campgrounds/' + campground._id);
              }
          });
        }
    });
    //create new comments
    //connect new comments to campground
    //redirect to campground show page
});


app.listen(3000, function() {
    console.log("Server connected!");
});
