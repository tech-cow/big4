// VARIABLE
var bodyParser       = require("body-parser"),
    methodOverride   = require("method-override"),
    expressSanitizer = require("express-sanitizer"),
    mongoose         = require("mongoose"),
    express          = require("express"),
    app              = express();


// APP CONFIG
mongoose.connect("mongodb://localhost/restful_blog_app");
app.set("view engine","ejs");
// app.use(express.static("public"));
app.use(express.static(__dirname + "/public"));
app.use(bodyParser.urlencoded({extended:true}));
app.use(expressSanitizer());
app.use(methodOverride("_method"));

// MONGOOSE/MODEL CONFIG
var blogSchema = new mongoose.Schema({
    title: String,
    image: String,
    body :  String,
    created: {type: Date, default: Date.now}
});

var Blog = mongoose.model("Blog", blogSchema);



/*********** RESTFUL ROUTES ***********/

app.get("/", function(req,res){
    res.redirect("/blogs");
});

// #1: INDEX ROUTE
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


// #2: NEW ROUTE
app.get("/blogs/new", function(req,res){
    res.render("new")
});

// #3: CREATE ROUTE
app.post("/blogs", function(req,res){
    //Sanitize JS Script Tag
    req.body.blog.body = req.sanitize(req.body.blog.body);
    //Create blog...
    Blog.create(req.body.blog, function(err, newBlog){
      if (err) {
          res.render("new")
      } else {
          res.redirect("/blogs")
      }
    });
});

// #4 SHOW ROUTE
app.get("/blogs/:id", function(req,res){
    // blog.findById(id, callback)
    Blog.findById(req.params.id, function(err, foundBlog){
        if (err) {
            res.redirect("/blogs");
        } else {
            res.render("show", {blog: foundBlog});
        }
    });
});

// #5 EDIT ROUTE
app.get("/blogs/:id/edit",function(req,res){
  Blog.findById(req.params.id, function(err, foundBlog){
      if (err) {
          res.redirect("/blogs");
      } else {
          res.render("edit", {blog: foundBlog});
      }
    });
});

// #6 UPDATE ROUTE
app.put("/blogs/:id", function(req,res){
    req.body.blog.body = req.sanitize(req.body.blog.body);
    // Blog.findByIdAndUpdate(id, newData, callback)
    Blog.findByIdAndUpdate(req.params.id, req.body.blog, function(err, updatedBlog){
        if (err) {
            res.redirect("/blogs");
        } else {
            res.redirect("/blogs/" + req.params.id);
        }
    });
});

// #7 DESTROY ROUTE
app.delete("/blogs/:id", function(req,res){
    Blog.findByIdAndRemove(req.params.id, function(err){
        if (err) {
          res.redirect("/blogs");
        } else {
          res.redirect("/blogs");
        }
    });
});


// SERVER
app.listen(3000,function(){
  console.log("Blog is connected");
});
