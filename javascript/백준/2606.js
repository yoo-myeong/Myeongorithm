const fs = require('fs')

// const input = fs.readFileSync('../../dev/stdin').toString().trim().split('\n')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const computerCnt = parseInt(input[0])
const computerCoupleCnt = parseInt(input[1])
const computerCouple = input.slice(2).map(it => {
    const nums = it.split(' ')
    return [parseInt(nums[0]), parseInt(nums[1])]
})
// console.log(computerCouple);

const visited = {}
const networkMap = {}
computerCouple.forEach(it => {
    const first = it[0]
    const second = it[1]

    visited[it[0]] = false
    visited[it[1]] = false

    if (networkMap[first]) networkMap[first].push(second)
    else networkMap[first] = [second]

    if (networkMap[second]) networkMap[first].push(first)
    else networkMap[second] = [first]
})

const bfs = (box) => {

    let answer = 0
    let queues = [1]
    visited[1] = true

    while (queues.length !== 0) {
        const q = queues.shift()
        const childs = box[q]

        childs.forEach(it => {
            if (!visited[it]) {
                visited[it] = true
                queues.push(it)
                answer += 1
            }
        })
    }

    return answer
}


const answer = bfs(networkMap)
// console.log(visited)
console.log(answer)
