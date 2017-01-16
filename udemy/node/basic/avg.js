var total = 0;
function avg(score){
  for (var i = 0; i < score.length; i++) {
    total = total + score[i];
  }
  console.log(Math.floor(total / score.length)); 
}

var score = [90, 98 , 89, 100, 100, 86, 94]
avg(score);
