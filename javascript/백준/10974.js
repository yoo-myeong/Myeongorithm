const fs = require("fs")

// const input = fs.readFileSync("/dev/stdin").toString()
const input = fs.readFileSync("../../dev/stdin").toString()

const num = parseInt(input)

const getPermutation = (arr, targetLength) => {
    let output = []

    function permutate (rests, perm) {
        if (perm.length === targetLength) {
            return output.push(perm)
        }

        rests.forEach((v, i) => {
            const rest = [...rests.slice(0, i), ...rests.slice(i+1)]
            permutate(rest, [...perm, v])
        })
    }

    permutate(arr, [])
    return output
}

let arr = []
for (let i = 1; i<=num; i++) arr.push(i)
const permutations = getPermutation(arr, num)

permutations.forEach(it => {
    console.log(it.join(' '))
})
