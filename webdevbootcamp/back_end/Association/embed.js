var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/blog_demo');
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
   posts: [postSchema]
});
var User = mongoose.model('User', userSchema);

/** createPost
postModel.create({
    title: "Sleep",
    content: "I sleep too much"
}, function(err,post){
    console.log(post);
})
*/

/** Create User
var newUser = new User({
    email: "Jon@gmail.com",
    name: "Jon"
});

newUser.posts.push({
    title: "Jon, give me a job",
    content:  "ya you heard me!!!!!!!"
});

newUser.save(function(err,user){
    if (err) {
        console.log(err);
    } else {
        console.log(user);
    }
});
*/


User.findOne({name: "Yu Zhou"}, function(err,user){
    if (err) {
        // console.log(err);
    } else {
        user.posts.push({
            title: "3 thing I hate",
            content: "not be able to help others * 3 "
        });
        user.save(function(err,user){
          if (err) {
              console.log(err);
          } else {
              console.log(user);
          }
        });
    }
});
