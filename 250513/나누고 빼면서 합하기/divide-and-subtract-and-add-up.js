const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");
const [n, m] = input[0].split(" ").map(Number);
const A = input[1].split(" ").map(Number);
// Please Write your code here.

// m 이 1이 될때까지 홀수면 -1 짝수면 /2 A의 m번째 원소를 계속 더해
function f(){
    let sum = 0
    let mm = m
    while(mm !== 1){
        sum += A[mm-1]
        if(mm%2 == 0){
            mm = mm/2
        }
        else{
            mm -= 1
        }
    }
    sum += A[0]    
    return sum
}

let result = 0
result = f()
console.log(result)
