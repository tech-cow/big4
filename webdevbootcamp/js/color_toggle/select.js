// var isPink = false;
//
// var byid = document.getElementById("highlight");
// var byclass = document.getElementsByClassName("special")[0];
// // var bytag = document.getElementsByTagName("li")
// var byquerySelector = document.querySelector("li");
// var byquerySelector2 = document.querySelector("#highlight");

var button = document.getElementsByTagName("button")[0];

/******************************First Attempt**************************/
// button.addEventListener("click",function()
//   {
//     if(isPink){
//       document.body.style.backgroundColor = "white";
//       // isPink = false;
//     }else{
//       document.body.style.backgroundColor = "pink";
//       // isPink = true;
//     }
//     // Toggle between colors
//     isPink = !isPink;
//   });

/******************************Better Attempt**************************/
//toggle between colors
button.addEventListener("click",function(){
  //takes in css class pink, and toggle it on the click button
  document.body.classList.toggle("pink");
});
