var express = require("express");
var router = express.Router();
var Campground = require('../models/campground');

/*===================
   CAMPGROUNDS ROUTE
====================*/

/* 1. INDEX ROUTE */
router.get("/campgrounds", function(req, res) {
    Campground.find({}, function(err, allCampgrounds) {
        if (err) {
            console.log(err);
        } else {
            res.render("campgrounds/index", {campgrounds: allCampgrounds});
        }
    });
});

/* 2. NEW ROUTE */
router.get("/campgrounds/new", function(req, res) {
    res.render("campgrounds/new");
});

/* 3. CREATE ROUTE */
router.post("/campgrounds", function(req, res) {
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
router.get("/campgrounds/:id", function(req, res) {
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

module.exports = router;
