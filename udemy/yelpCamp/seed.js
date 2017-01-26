//SEEDING CAMPGROUNDS
var mongoose = require('mongoose'),
  Compground = require('./models/campground'),
  Comment     = require('./models/comment');

var data = [
    {
        name: "Snot Camping",
        image: "http://www.thatsnotcamping.com/wp-content/uploads/2012/02/White-Memorial-Foundation-Family-Campgrounds.jpg",
        description: "cool campground"
    },
    {
        name: "Cons Camping",
        image: "http://www.conservacionpatagonica.org/images/pic_campgrounds_02.jpg",
        description: "meh campground"
    },
    {
        name: "Green Camping",
        image: "http://www.greenvalleycamp.com/images/Green_Valley_Campgrounds_011.jpg",
        description: "Damm campground"
    }
];

function seedDB(){
    // *1* Remove all Campgrounds
    Compground.remove({},function(err){
        if (err) {
          console.log(err);
        } else {
          console.log("removed campgrounds");
          // *2* Add a few Campgrounds
          data.forEach(function(seed){
            Compground.create(seed, function(err,campground){
              if (err) {
                  console.log(err);
              } else {
                  console.log('Added a campground');
                  Comment.create(
                    {
                        text: "Wow, this suck!",
                        author: "Yu"
                    }, function(err, comment){
                        if (err) {
                            console.log(err);
                        } else {
                            campground.comments.push(comment);
                            campground.save();
                            console.log("creating new comments");
                        }
                    });
              }
            });
          });
        }
    });

    // *3* Add a few Campgrounds



}

module.exports = seedDB;
