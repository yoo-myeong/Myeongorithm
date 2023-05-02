const fs = require('fs')

/////////////////////////////////////////////////
// const input = fs.readFileSync('./dev/stdin').toString().trim().split('\n')
/////////////////////////////////////////////////

/////////////////////////////////////////////////
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
/////////////////////////////////////////////////

const n = input[0]
const numbers = input[1].split(' ').map(it => parseInt(it))
const symbolCnts = input[2].split(' ').map(it => parseInt(it))

const getPermutations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el])

    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index+1)] 
      const permutations = getPermutations(rest, selectNumber - 1)
      const attached = permutations.map((el) => [fixed, ...el])
      results.push(...attached)
    })

    return results
}


// console.log(n)
// console.log(numbers)
// console.log(symbols)

const numLength = numbers.length
const symLength = numLength - 1

let symbols = []
symbolCnts.forEach((cnt, index) => {
    for(let i=0; i<cnt; i++) symbols.push(index)
})
// console.log(symbols)

/** @type {[]} */
const combi = getPermutations(symbols, symLength)

// console.log(combi)

const testCaseCnt = combi.length

let maxVal = -1e9
let minVal = 1e9

for (let i = 0; i < testCaseCnt; i++) {
    const applySymbols = combi[i]
    const sum = numbers.reduce((acc, cur, index)=>{
        if(index === 0) return acc+cur
        
        const symbol = applySymbols[index - 1]
        
        if(symbol === 0) {
            return cur + acc
        } else if (symbol === 1) {
            return cur - acc
        } else if (symbol === 2) {
            return cur * acc
        } else {
            return parseInt(cur / 2)
        }
    }, 0)
    // console.log(sum)
    maxVal = Math.max(maxVal, sum)
    minVal = Math.min(minVal, sum)

    // console.log(`maxVal=${maxVal}`)
    // console.log(`minVal=${minVal}`)
}

console.log(maxVal)
console.log(minVal)
