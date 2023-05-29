const fs = require('fs')

// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const input = fs.readFileSync('./dev/stdin').toString().trim().split('\n')
const [n,m] = input[0].split(' ').map(it => parseInt(it))
const arr = input[1].split(' ').map(it => parseInt(it))
// console.log(n,m,arr)

/**
 * @param {number} n 
 * @param {number} m 
 * @param {number[]} arr 
 */
const solution = (n, m, arr) => {
    const length = arr.length

    let cnt = 0

    for(let i = 0; i<length-1 ; i++){
        let sum = arr[i]
        if(sum === m) cnt ++
        for(let j = i+1; j<length; j++) {
            // console.log(i,j,arr[i],arr[j])
            sum += arr[j]
            // console.log(`=${sum}`)
            if(sum === m) cnt ++
        }
    }

    if(arr[n-1] === m) cnt ++

    return cnt
}
// console.log(solution(10, 5, [1,2,3,4,2,5,3,1,1,2]))
console.log(solution(n,m,arr))
