// VARIABLE
var bodyParser = require("body-parser"),
    mongoose   = require("mongoose"),
    express    = require("express"),
    app        = express();


// APP CONFIG
mongoose.connect("mongodb://localhost/restful_blog_app");
app.set("view engine","ejs");
// app.use(express.static("public"));
app.use(express.static(__dirname + "/public"));
app.use(bodyParser.urlencoded({extended:true}));


// MONGOOSE/MODEL CONFIG
var blogSchema = new mongoose.Schema({
    title: String,
    image: String,
    body :  String,
    created: {type: Date, default: Date.now}
});
var Blog = mongoose.model("Blog", blogSchema);


// RESTFUL ROUTES
app.get("/", function(req,res){
    res.redirect("/blogs");
});

app.get("/blogs", function(req,res){
    // retreive data from the database
    Blog.find({}, function(err,blogs){
      if (err) {
          console.log("ERROR!");
      } else {
        // pass data to ejs for rendering
          res.render("index", {blogs:blogs});
      }
    });
});

app.listen(3000,function(){
  console.log("Blog is connected");
});
