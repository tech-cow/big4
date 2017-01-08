/************Main***********/
// Make an array
var todo_array = ["Buy a cup of tea"];
// Prompt for command

var input = prompt("What can I do for you?");

while (input !== "quit") {
  if (input === "list") {
    listTodos();
  } else if(input === "new") {
    newTodos();
  } else if (input === "delete") {
    deleteTodos();
    }
  input = prompt("What can I do for you?");
}
console.log("OK,I QUIT FOR YOUUUUU");


/************Function definitions***********/
function listTodos(){
  console.log("**********");
  todo_array.forEach(function(todo, index){
    console.log(index + ": " + todo);
  });
  console.log("**********");
}

function newTodos(){
  var new_todo = prompt("Ok, what activity would you like to add?");
  todo_array.push(new_todo);
}

function deleteTodos(){
  var array_index = prompt("Which Todo are you willing to erase?")
  // todo_array.pop(array_index);
  todo_array.splice(array_index, 1)
  console.log("Deleted Todo");
}
