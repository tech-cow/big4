// VARIABLE
var express     = require('express'),
    mongoose    = require('mongoose'),
    bodyParser  = require('body-parser'),
    methodOverride = require('method-override'),
    app         = express();


// APP CONFIG
mongoose.connect('mongodb://localhost/findpal');
app.set("view engine","ejs");
app.use(express.static(__dirname + "/public"));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(methodOverride('_method'));



/*********** MONGOOSE/MODEL CONFIG ***********/

// define a schema
var blogSchema = mongoose.Schema({
    title: String,
    image: String,
    location: String,
    wechat: String,
    body: String,
    created: {type: Date, default: Date.now}
});

// create a mondel
var Blog = mongoose.model('Blog', blogSchema);

/**
  *TEST*
  Blog.create({
    title: "Martinez狼人杀",
    image: "http://tc.sinaimg.cn/maxwidth.800/tc.service.weibo.com/mmbiz_qpic_cn/a7a40e2f7021f2306bc7dccb3281399f.jpg",
    location: "Martinez",
    wechat: "woaini321",
  });
*/

/*********** RESTFUL ROUTES ***********/
app.get("/",function(req,res){
    res.redirect('/blogs');
});

// #1: INDEX ROUTE
app.get("/blogs",function(req,res){
  // *1* get data from database
  Blog.find({}, function(err,foundData){
      if (err) {
          res.redirect("/blogs")
      } else {
          // *2* pass data to the rendered page
          res.render('index', {blogs: foundData})
      }
  });
});


// #2: NEW ROUTE
app.get("/blogs/new",function(req,res){
    res.render("new");
});


// #3: CREATE ROUTE
app.post("/blogs", function(req,res){
  // *1* Gather data from the name attribute in form (I named it blog)
  Blog.create(req.body.blog, function(err, newBlog){
      if (err) {
          res.render("new")
      } else {
        // *2* Post it back (redirect) to the blog site
          res.redirect("/blogs");
      }
  })
});

// #4 SHOW ROUTE
app.get("/blogs/:id", function(req,res){
  Blog.findById(req.params.id, function(err,foundData){
      if (err) {
          res.redirect("/blogs")
      } else {
          // *2* pass data to the rendered page
          res.render('show', {blog: foundData})
      }
  });
});

// #5 EDIT ROUTE
app.get('/blogs/:id/edit', function(req,res){
    // *1* retreive data for specific id
    Blog.findById(req.params.id, function(err,foundData){
        if (err) {
            res.redirect("/blogs")
        } else {
            // *2* pass data to the rendered page
            res.render('edit', {blog: foundData})
        }
    });
});

// #6 UPDATE ROUTE
app.put('/blogs/:id', function(req,res){
    Blog.findByIdAndUpdate(req.params.id, req.body.blog, function(err, updatedData){
      if (err) {
        res.redirect("/blogs")
      } else {
        res.redirect("/blogs")
      }
    });
});

// #7 DESTROY ROUTE


// SERVER
app.listen(3000,function(){
  console.log("Blog is connected");
});
