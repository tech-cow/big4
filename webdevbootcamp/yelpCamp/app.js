/*===================
   VARIABLES
====================*/
var express = require("express"),
    app = express(),
    bodyParser = require("body-parser"),
    mongoose = require("mongoose"),
    passport = require('passport'),
    User = require('./models/user'),
    LocalStrategy = require('passport-local'),
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

/* PASSPORT CONFIG */
app.use(require('express-session')({
      secret: "Rusty sucks",
      resave: false,
      saveUninitialized: false,
}));

app.use(passport.initialize());
app.use(passport.session());
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());



/*===================
   CAMPGROUNDS ROUTE
====================*/

app.get("/", function(req, res) {
    res.render("home");
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

});

/*===================
 AUTHENTICATION ROUTE
====================*/

/* SIGN-UP ROUTE */
app.get('/register', function(req,res){
      res.render('register');
});

// Handler
app.post('/register', function(req,res){
    var newUser = new User({username: req.body.username});
    User.register(newUser, req.body.password, function(err, user){
        if (err) {
              console.log(err);
              return res.render("register");
        }
        //log user in here. this code repeat later in log in route
        passport.authenticate("local")(req, res, function(){
          res.redirect("/campgrounds");
        });
    });
});


/* LOGIN ROUTE */
app.get('/login',function(req,res){
    res.render('login');
});

//app.post("/login", middleware, function)
app.post("/login", passport.authenticate("local",
    {
        successRedirect: '/campgrounds',
        failureRedirect: '/login'
    }), function(req,res){
});




app.listen(3000, function() {
    console.log("Server connected!");
});
