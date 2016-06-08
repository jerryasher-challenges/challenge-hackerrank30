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
  if (input_currentline < input_stdin_array.length) {
    return input_stdin_array[input_currentline++];
  } else {
    return false;
  }
}

/////////////// ignore above this line ////////////////////

function main() {
  var N = parseInt(readLine());
  var statement = "";
  var phonebook = {};
  for (var i = 0; i < N; i++) {
    var line = readLine();
    var pair = line.split(" ");
    phonebook[pair[0]] = pair[1];
  }

  while (query = readLine()) {
    if (query in phonebook) {
      process.stdout.write(query + "=" + phonebook[query]);
    } else {
      process.stdout.write("Not found");
    }
    process.stdout.write("\n");
  }

}

