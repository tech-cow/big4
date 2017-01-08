


// Make an array
var todo_array = [];
// Prompt for command

var input = prompt("What can I do for you?");

while (input !== "quit") {
  input = prompt("What can I do for you?");
  if (input === "new") {
      var new_todo = prompt("Ok, what activity would you like to add?");
      todo_array.push(new_todo);
    }
  else if (input === "list") {
    console.log(todo_array);
  }
}
