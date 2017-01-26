var mongoose = require("mongoose");
//CAMPGROUNDS SCHEMA SETUP
var commentSchema = new mongoose.Schema({
    text: String,
    author: String,
});

module.exports = mongoose.model("Comment", commentSchema);
