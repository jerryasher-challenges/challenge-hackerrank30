
function processData(inputString) {
    // Your first line of output goes here
    process.stdout.write("Hello, World.\n");
    
    // Write the second line of output
    process.stdout.write(inputString);
} 


process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
