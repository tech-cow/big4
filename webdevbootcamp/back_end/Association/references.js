var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/blog_demo_2');
var Schema = mongoose.Schema;


//POST - title, content
var postSchema = new Schema({
   title: String,
   content: String
});
postModel = mongoose.model('Post', postSchema);


//USER - email, name
var userSchema = new Schema({
   email: String,
   name: String,
   posts: [
      {
          type: mongoose.Schema.Types.ObjectId,
          ref: "Post"
      }
   ]
});
var User = mongoose.model('User', userSchema);

//CREATE
User.create({
    email: "bob@gmail.com",
    name: "Bob Belcher"
},function(err,user){
    console.log(user);
});
