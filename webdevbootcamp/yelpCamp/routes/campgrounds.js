var express = require("express");
var router = express.Router();
var Campground = require('../models/campground');

/*===================
   CAMPGROUNDS ROUTE
====================*/

/* 1. INDEX ROUTE */
router.get("/",  function(req, res) {
    Campground.find({}, function(err, allCampgrounds) {
        if (err) {
            console.log(err);
        } else {
            res.render("campgrounds/index", {campgrounds: allCampgrounds});
        }
    });
});

/* 2. CREATE ROUTE */
router.post("/", isLoggedIn, function(req, res) {
    var name  =  req.body.name,
        image =  req.body.image,
        desc  =  req.body.description,
        author = {
            id: req.user._id,
            username: req.user.username
        };
    var newCampground = {name: name, image: image, description: desc, author: author};

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

/* 3. NEW ROUTE */
router.get("/new", isLoggedIn, function(req, res) {
    res.render("campgrounds/new");
});

/* 4. SHOW ROUTE */
router.get("/:id",isLoggedIn, function(req, res) {
  Campground.findById(req.params.id).populate("comments").exec(function(err, foundCampground) {
        if (err) {
            console.log(err);
        } else {
            // console.log(foundCampground);
            res.render("campgrounds/show", {campground: foundCampground});
        }
    });
});

/* 5. EDIT ROUTE */
router.get('/:id/edit',checkCampgroundOwndership, function(req,res){
    Campground.findById(req.params.id, function(err, foundCampground){
        res.render("campgrounds/edit", {campground:foundCampground});
    });

});


/* 6. UPDATE ROUTE */
router.put("/:id", checkCampgroundOwndership, function(req,res){
    //find and update the correct

    Campground.findByIdAndUpdate(req.params.id, req.body.campground, function(err, updatedCampground){
        if(err){
            res.redirect("/campgrounds");
          } else {
            //redirect somewhere(show page)
            res.redirect("/campgrounds/" + req.params.id);
      }
    });
    //redirect

});

/* 7. DESTROY ROUTE */
router.delete("/:id", checkCampgroundOwndership, function(req,res){
    Campground.findByIdAndRemove(req.params.id, function(err){
        if (err) {
          res.redirect("/campgrounds");
        } else {
          res.redirect("/campgrounds");
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


function checkCampgroundOwndership(req,res,next){
  if (req.isAuthenticated()) {
      Campground.findById(req.params.id, function(err, foundCampground){
          if (err) {
              res.redirect("/campgrounds");
          } else {
            // does user own the compground?
            if (foundCampground.author.id.equals(req.user._id)) {
                next();
            } else {
                res.redirect('back');
            }
          }
      });
    } else {
          res.redirect('back');
    }
}



module.exports = router;
