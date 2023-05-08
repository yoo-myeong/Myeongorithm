const fs = require('fs')

// const input = fs.readFileSync('./dev/stdin').toString().trim().split('\n')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [h,w] = input[0].split(' ').map(it => parseInt(it))
const blockHeights = input[1].split(' ').map(it => parseInt(it))

let answer = 0
let mostHeight = -1e9

for (const [index, height] of blockHeights.entries()) {

    if (index === 0 || index === blockHeights.length-1) continue

    const leftSlicedHeigths = blockHeights.slice(0, index)
    const rigthSlicedHeights = blockHeights.slice(index+1)
    // console.log(`------${index}------`)
    // console.log(leftSlicedHeigths)
    // console.log(rigthSlicedHeights)

    const maxLeftHeigths = Math.max(...leftSlicedHeigths)
    const maxRightHeights = Math.max(...rigthSlicedHeights)
    // console.log(`maxLeftHeigths=${maxLeftHeigths}`)
    // console.log(`maxRightHeights=${maxRightHeights}`)

    const minHeight = Math.min(maxLeftHeigths, maxRightHeights)
    // console.log(index,minHeight)

    const gap = minHeight - height

    if(gap > 0) answer += gap

}

console.log(answer)