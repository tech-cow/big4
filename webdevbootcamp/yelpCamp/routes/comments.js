var express = require("express");
var router = express.Router();
var Campground = require('../models/campground');
var Comment = require('../models/comment');
/*===================
   COMMENTS ROUTE
====================*/

/* 1. NEW ROUTE */
router.get("/campgrounds/:id/comments/new", isLoggedIn, function(req,res){
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
router.post("/campgrounds/:id/comments", function(req,res){
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
     MIDDLEWARE
====================*/
function isLoggedIn(req,res,next){
    if(req.isAuthenticated()){
        return next();
    }
    res.redirect("/login");
}


module.exports = router;
