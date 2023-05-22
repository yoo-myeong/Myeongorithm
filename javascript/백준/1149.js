const fs = require("fs")

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const n = parseInt(input[0])
const box = input.slice(1).map(it => it.split(' ').map(num => parseInt(num)))

// console.log(box)

const getPermutation = (arr) => {
    let output = []

    function permutate(rests, perm) {
        if(perm.length === arr.length) return output.push(perm)

        rests.forEach((r, i) => {
            const newPerm = [...perm, r]
            // const rest = [...rests.slice(0, i), ...rests.slice(i+1)]
            permutate(rests, newPerm)
        })
    }

    permutate(arr, [])

    return output
}

let arr = []
for(let i=0; i<n; i++) arr.push(i)
const permutations = getPermutation(arr)
// console.log(permutations)

const filterValidPerm = (perms, housesCnt) => {
    const validPerms = perms.filter(perm => {
        return ( 
            perm[0] !== perm[1] &&
            perm[housesCnt-1] !== perm[housesCnt-2] &&
            perm.slice(2, housesCnt-1).every((p, index) => {
                p !== perms[index-1] && p !== perms[index+1]
            })
        )
    })

    return validPerms
}

const validPerms = filterValidPerm(permutations, n)
// console.log(validPerms)

const caculateCost = (perm) => {
    let cost = 0
    perm.forEach((color, houseNum) => {
        cost += box[houseNum][color]
    })
    return cost
}
// console.log(validPerms[0])
// console.log(caculateCost(validPerms[0]))

let answer = 1e9
validPerms.forEach(perm => {
    const cost = caculateCost(perm)
    answer = Math.min(answer, cost)
})
console.log(answer)