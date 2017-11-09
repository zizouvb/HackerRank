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

function timeConversion(s) {
    // Complete this function
    if (s.substring(s.length-2,s.length)==="PM" && parseInt(s.substring(0,2)) !== 12)
    {
        var h = parseInt(s.substring(0,2)) + 12;
        s  = h.toString() + s.substring(2,10);
    }
    else if (parseInt(s.substring(0,2)) === 12 && s.substring(s.length-2,s.length)==="AM") 
    { 
        var h = 0;
        s  = "00" + s.substring(2,10);
    }    
    return s.substring(0,8)
}

function main() {
    var s = readLine();
    var result = timeConversion(s);
    process.stdout.write("" + result + "\n");

}

