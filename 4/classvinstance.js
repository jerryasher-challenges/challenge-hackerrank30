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

function Person(initialAge) {
  if (initialAge >= 0) {
    this.age = initialAge;
  } else {
    process.stdout.write("Age is not valid, setting age to 0.\n")
    this.age = 0;
  }

  // Add some more code to run some checks on initialAge
  this.amIOld=function(){
    if (this.age < 13) {
      process.stdout.write("You are young.\n");
    }
    else if (this.age < 18) {
      process.stdout.write("You are a teenager.\n");
    }
    else {
      process.stdout.write("You are old.\n");
    }

  };
  this.yearPasses=function(){
    // Increment the age of the person in here
    this.age++;
  };
}
