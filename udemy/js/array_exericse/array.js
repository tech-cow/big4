/************Test***********/
/*printReverse*/
printReverse(["1","2","3","4"]);
printReverse([1,3,4,9]);

/*sumArray*/
sumArray([1,3,4,9]);
sumArray([1,1,1,1]);

/*max*/
max([100,1,3,4,9,10]);
max([20000,200,100,9]);


/************Function definitions***********/
function printReverse(input_array){
  var reversed_array = [];
  for (var i = input_array.length-1; i >= 0; i--) {
    reversed_array.push(input_array[i])
  }
  console.log(reversed_array);
}

function isUniform(arr){
  var first = arr[0];
  for (var i = 1; i < arr.length-1; i++) {
    if (arr[i] !== first) {
      return false;
    }
  }
  return true;
  }

function sumArray(arr){
  var result = 0;
  for (var i = 0; i < arr.length; i++) {
    result = arr[i] + result;
  }
  console.log(result);
}

function max(arr){
  var max = arr[0];
  for (var i = 1; i < arr.length; i++) {
    if (arr[i] >= max) {
      max = arr[i];
    }
  }
  console.log(max);
  // return max;

}
