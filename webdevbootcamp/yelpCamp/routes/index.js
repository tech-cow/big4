var express = require("express");
var router = express.Router();
var passport = require('passport');
var User = require('../models/user');

/* ROOT ROUTE */
router.get("/", function(req, res) {
    res.render("home");
});

/*===================
 AUTHENTICATION ROUTE
====================*/
/* SIGN-UP ROUTE */
router.get('/register', function(req,res){
      res.render('register');
});

/* SIGN-UP HANDLER */
router.post('/register', function(req,res){
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
router.get('/login',function(req,res){
    res.render('login');
});

/* LOGIN HANDLER */
router.post("/login", passport.authenticate("local",
    {
        successRedirect: '/campgrounds',
        failureRedirect: '/login'
    }), function(req,res){
});

/* LOG OUT ROUTE */
router.get('/logout',function(req,res){
    req.logout();
    res.redirect('/campgrounds');
});


/*===================
     MIDDLEWARE
====================*/
function isLoggedIn(req,res,next){
    if(req.isAuthenticated()){
        return next();
    }
    res.redirect("/login");
}

module.exports = router;
