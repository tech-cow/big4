/*===================
   VARIABLES
====================*/
var express           = require("express"),
    app               = express(),
    bodyParser        = require("body-parser"),
    mongoose          = require("mongoose"),
    passport          = require('passport'),
    User              = require('./models/user'),
    LocalStrategy     = require('passport-local'),
    Campground        = require("./models/campground"),
    Comment           = require("./models/comment"),
    seedDB            = require("./seed");

var commentRoutes     = require('./routes/comments'),
    campgroundRoutes  = require('./routes/campgrounds'),
    indexRoutes       = require('./routes/index');

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

app.use(function(req,res,next){
    res.locals.currentUser = req.user;
    next();
});

/* ROUTES CONFIG */
app.use(indexRoutes);
app.use(campgroundRoutes);
app.use(commentRoutes);

/*===================
        SERVER
====================*/
app.listen(3000, function() {
    console.log("Server connected!");
});
