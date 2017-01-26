/**Variable**/
var input = document.querySelector('#input');
var p1_button = document.querySelector("#p1");
var p2_button = document.querySelector("#p2");
var reset_buttom = document.querySelector("#reset");
var p1_display = document.querySelector("#p1_display");
var p2_display = document.querySelector("#p2_display");
var winning_score_display = document.querySelector("#score_display");
var p1_score = 0;
var p2_score = 0;
var winning_score = 5;
var game_over = false;

// var score_display= document.querySelector("score");
// var score = 0;


/**Event**/

input.addEventListener('change', function() {
  winning_score_display.textContent = input.value;
  winning_score = Number(input.value);
  reset();
});

p1_button.addEventListener('click', function() {
  if(!game_over){
    p1_score++;
    if (p1_score === winning_score) {
      p1_display.classList.add("winner");
      game_over = true;
    }
  }
  p1_display.textContent = p1_score;
});

p2_button.addEventListener('click', function() {
  if(!game_over){
    p2_score++;
    if (p2_score === winning_score) {
      p2_display.classList.add("winner");
      game_over = true;
    }
  }
  p2_display.textContent = p2_score;
});


reset_buttom.addEventListener('click', function() {
  reset();
});



/**Function**/
function reset(){
  p1_score = 0;
  p2_score = 0;
  p1_display.textContent = 0;
  p2_display.textContent = 0;
  p1_display.classList.remove("winner");
  p2_display.classList.remove("winner");
  game_over = false;
}
