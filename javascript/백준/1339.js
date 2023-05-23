const fs = require('fs')

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./dev/stdin').toString().trim().split('\n')

const n = parseInt(input[0])
const words = input.slice(1).map(word => word.split(''))
// console.log(words)
const alphabets = new Set(words.flatMap(it => it))
const numbers = ['0','1','2','3','4','5','6','7','8','9']
// alphabets.forEach(i => console.log(i))

let cnt = 0
const getPermutations = (targetLength, arr) => {
    let output = []

    /**
     * @param {number[]} rests 
     * @param {number[]} perm 
     * @returns 
     */
    function permutate(rests, perm) {
        if(perm.length === targetLength) return output.push(perm)

        rests.forEach((v,i) => {
            cnt += 1
            const rest = [...rests.slice(0, i), ...rests.slice(i+1)]
            permutate(rest, [...perm, v])
        })
    }

    permutate(arr, [])
    // console.log({cnt})
    return output
}

const permutations = getPermutations(alphabets.size, numbers)
// console.log(getPermutations(alphabets.size, numbers))
// console.log(permutations.length)

let answer = -1e9
permutations.forEach(permutation => {
    const numMapByAlphabet = new Map()
    alphabets.forEach(alphabet => numMapByAlphabet.set(alphabet, permutation.pop()))

    const value1 = words[0].reduce((acc, cur) => acc + numMapByAlphabet.get(cur), 0)
    const value2 = words[1].reduce((acc, cur) => acc + numMapByAlphabet.get(cur), 0)

    // console.log({value1, value2})
    answer = Math.max(answer, parseInt(value1) + parseInt(value2))
})

console.log(answer)

// const permutation = ['0', '1', '2', '3', '8', '9', '7']
// const numMapByAlphabet = new Map()
// alphabets.forEach(alphabet => numMapByAlphabet.set(alphabet, permutation.pop()))

// const value1 = words[0].reduce((acc, cur) => acc + numMapByAlphabet.get(cur), '')
// const value2 = words[1].reduce((acc, cur) => acc + numMapByAlphabet.get(cur), '')

// console.log({value1, value2})