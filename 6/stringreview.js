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

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

function walk(line) {
  var first = [];
  var second = [];
  for (i = 0; i < line.length; i++) {
    if (i % 2 == 0) {
      first.push(line[i]);
    } else {
      second.push(line[i]);
    }
  }
  var out = first.join("") + " " + second.join("");
  return out;
}

function main() {
  var N = parseInt(readLine());
  var statement = "";
  for (var i = 1; i <= N; i++) {

    var line = readLine();
    statement = walk(line) + "\n";
    process.stdout.write(statement);
  }
}

