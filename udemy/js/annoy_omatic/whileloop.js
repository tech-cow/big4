var user_input = prompt("You love me ?")

while(user_input !== "Yes" && user_input !== "yes" && user_input.indexOf("yes") === -1){
  var user_input = prompt("You love me ?")
}

alert("I love myself too");
