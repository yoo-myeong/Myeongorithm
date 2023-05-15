const fs = require("fs")

const input = fs.readFileSync("/dev/stdin").toString()
// const input = fs.readFileSync("./dev/stdin").toString()

const num = parseInt(input)

let arr = []
for (let i = 0; i < num; i++) arr.push(i+1)
// console.log(arr)

/**
 * @param {number[]} perm 
 * @param {number[]} rests 
 * @param {number[][]} output 
 * 
 * @return {number[][]}
 */
const getPermutation = (perm, rests, output) => {
    if (rests.length === 0) {
        return output.push(perm)
    }

    rests.forEach((value, index) => {
        const rest = [...rests.slice(0, index), ...rests.slice(index+1)]
        getPermutation([...perm, value], rest, output)
    })
}

const output = []
getPermutation([], arr, output)

// console.log(output)
output.forEach(perm => {
    console.log(perm.join(' '))
})