const fs = require("fs")

// const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const num = parseInt(input[0])

function getMinPermutations(n) {
    let permutations = []

    const permutate = (rest, cnt) => {
        if(rest === 1) return permutations.push(cnt)
        else if (rest > 1) {
            if(rest % 3 === 0) permutate(rest/3, cnt+1)
            if(rest % 2 === 0) permutate(rest/2, cnt+1)
            permutate(rest - 1, cnt+1)    
        }
    }

    permutate(n, 0)
    console.log(permutations)
    return Math.min(...permutations)
}

console.log(getMinPermutations(num))