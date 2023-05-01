const fs = require("fs")

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
const inputToNum = input.map(it => parseInt(it))

let answer = []
labelCancelLoops: while (true) {

    const sum = inputToNum.reduce((acc,cur) => acc + cur, 0)

    // console.log(`sum=${sum}`)

    for(let i = 0; i < inputToNum.length-1; i++) {
        for (let j = i+1; j <  inputToNum.length; j++) {
            const smallGuy1 = inputToNum[i]
            const smallGuy2 = inputToNum[j]

            // console.log(`smallGuy1=${smallGuy1}, smallGuy2=${smallGuy2}`)

            const leftSmallGuySum = sum - smallGuy1 - smallGuy2
            // console.log(`leftSmallGuySum=${leftSmallGuySum}`)
            if(leftSmallGuySum === 100) {
                answer = inputToNum.filter((it, index) => {
                    if(index !== i && index !== j) return true
                })
                break labelCancelLoops
            }

        }
    }
}

answer.sort((a,b)=> a-b).forEach(it => console.log(it))