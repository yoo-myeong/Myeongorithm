const fs = require("fs")
const { resourceLimits } = require("worker_threads")

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const testCaseCnt = input[0]
const nums = input.slice(1).map(it => parseInt(it))
// console.log(nums)

function getPermutations(nums, permLength) {
    let output = []
    // console.log(`getPermutations | ${JSON.stringify({nums, permLength})}`)

    const permutate = (rests, perm) => {
        // console.log(`permutate | ${JSON.stringify({rests, perm})}`)
        if(perm.length === permLength) {
            output.push(perm)
            return
        }

        rests.forEach((v, i) => {
            // console.log(`nums.forEach | ${v}, ${i}`)
            // const rest = [...rests.slice(0, i), ...rests.slice(i+1)]
            permutate(rests, [...perm, v])
        })
    }

    permutate(nums, [])
    return output
}

function isPermSumSameWithTarget(arr, target) {
    return arr.reduce((acc, cur) => acc + cur, 0) === target
}

/**
 * 
 * @param {number[][]} permutations 
 * @param {number} target 
 * 
 * @return {number}
 */
function getValidPermCnt(permutations, target) {
    let sum = 0
    permutations.forEach((perm) => {
        if(isPermSumSameWithTarget(perm, target)) sum ++
    })

    return sum
}

////////////////////////////////////////////////////////////////////////////////

try {
    const elements = [1,2,3]
    for (let i=0; i<testCaseCnt; i++) {
        const target = nums[i]
        let sum = 0
        for (let j=1; j<=target; j++) {
            const permutations = getPermutations(elements, j)
            // console.log(`answer | permutations = ${JSON.stringify(permutations)}`)
            sum += getValidPermCnt(permutations, target)
        }
        console.log(sum)
    }
} catch (error) {
    console.log(error)
}
