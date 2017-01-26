var mongoose = require("mongoose");
mongoose.Promise = global.Promise;
mongoose.connect("mongodb://localhost/cat_app");


//cat pattern
var catSchema = new mongoose.Schema({
    name: String,
    age: Number,
    temperament: String
});

//compile an model that has all of the methods to use
//models contain documents
var Cat = mongoose.model("Cat",catSchema);

//adding a new at to the DB

// var sam = new Cat({
//     name: "Bad",
//     age: 200 ,
//     temperament : "Evil"
// });
//
// sam.save(function(err, cat){
//     if(err){
//       console.log("Oops");
//     } else {
//       console.log("data Saved");
//       console.log(cat);
//     }
// });

//retrieve all cats from the DB and log each one
Cat.create({
    name: "Snow White",
    age: 15,
    temperament: "Bland"
}, function(err,cats){
  if (err) {
      console.log(err);
  } else {
      console.log(cats);
  }
})

Cat.find({},function(err, cats){
    if (err) {
      console.log("Oh nOOO!");
      console.log(err);
    } else {
      console.log("There we go , all the cats");
      console.log(cats);
    }
});
