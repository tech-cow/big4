var express                = require('express'),
    mongoose               = require('mongoose'),
    passport               = require('passport'),
    bodyParser             = require('body-parser'),
    User                   = require('./models/user'),
    LocalStrategy          = require('passport-local'),
    passportLocalMongoose  = require('passport-local-mongoose');


mongoose.connect('mongodb://localhost/auth_demo_app');
var app = express();
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: false }));
//session setup
app.use(require('express-session')({
      secret: "Rusty sucks",
      resave: false,
      saveUninitialized: false,
}));

//passport.js setup
app.use(passport.initialize());
app.use(passport.session());

passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

/*===================
        ROUTE
====================*/
app.get('/', function(req,res){
    res.render('home');
});

app.get('/secret', isLoggedIn, function(req,res){
    res.render('secret');
});


/*===================
     AUTH ROUTE
====================*/

/*SIGN UP*/
app.get("/register", function(req,res){
    res.render('register');
});

/*HANDLING USER SIGN UP*/
app.post("/register", function(req,res){
    User.register(new User({username: req.body.username}), req.body.password, function(err,user){
        if (err) {
            console.log(err);
            return res.render('register');
        }
        passport.authenticate("local")(req,res,function(){
            res.redirect("/secret");
        });
    });
});

/*LOG IN*/
app.get("/login", function(req,res){
    res.render('login');
});

/*HANDLING USER LOGIN*/
app.post("/login", passport.authenticate('local', {
    successRedirect:"/secret",
    failureRedirect:"login"
}), function(req,res){
});

/*LOG OUT*/
app.get("/logout", function(req,res){
    req.logout();
    res.redirect("/");
});

function isLoggedIn(req, res, next){
    if (req.isAuthenticated()) {
        return next();
    }
    res.redirect("/login");
}

/*SERVER*/
app.listen(3000, function(){
  console.log('Server working');
});
