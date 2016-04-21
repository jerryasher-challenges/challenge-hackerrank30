process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

// Reads complete line from STDIN
function readLine() {
    return input_stdin_array[input_currentline++];
}

function main() {

  var mealCost = parseFloat(readLine());  
  var tipPercent = parseInt(readLine());
  var taxPercent = parseInt(readLine());

  // Write your calculation code here.
  var cost = mealCost * (1.0 + (tipPercent + taxPercent) / 100.0);

  // cast the result of the rounding operation to an int and save it as totalCost
  var totalCost = Math.round(cost);

  // Print your result
  process.stdout.write("The total meal cost is " + totalCost + " dollars.");
}
