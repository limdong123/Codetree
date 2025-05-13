const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');
const [n, m] = input[0].split(" ").map(Number);
const A = input[1].split(" ").map(Number);
const queries = input.slice(2).map(line => line.split(" ").map(Number));

// Please write your code here.
function f(){
    for(i = 0; i < queries.length; i++){
        let sum = 0
        for(j = queries[i][0]; j <= queries[i][1]; j++){
            sum += A[j-1]
        }
        console.log(sum)
    }
}

f()
