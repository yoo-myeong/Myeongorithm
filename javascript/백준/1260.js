const fs = require("fs")

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [n,m,v] = input[0].split(' ').map(it => parseInt(it))
// console.log(n,m,v)
/**
 * @type {number[][]}
 */
const connectionInfo = input.slice(1).map(it => it.split(' ').map(it2 => parseInt(it2)))
// console.log(connectionInfo)

//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////

/**
 * @type {Map<number, number[]>}
 */
const connectionMap = new Map()

connectionInfo.forEach(it => {
    const [key, value] = it
    
    const mapValueByKey = connectionMap.get(key)

    if(mapValueByKey === undefined) {
        connectionMap.set(key, [value])
    } else {
        mapValueByKey.push(value)
    }

    const mapKeyByValue = connectionMap.get(value)

    if(mapKeyByValue === undefined) {
        connectionMap.set(value, [key])
    } else {
        mapKeyByValue.push(key)
    }
})

// connectionMap.forEach((v,k) => console.log(`key=${k}, value=${v}`))

function dfs(n) {
    const dfsVisited = {}
    let dfsVisitedNode = []
    function dfsInnerFunciton(n) {
        dfsVisited[n] = true
        dfsVisitedNode.push(n)

        const valueByKey = connectionMap.get(n)
        if (valueByKey) {
            valueByKey.sort((a,b) => a - b)
            valueByKey.forEach(nextNode => {
                if (dfsVisited[nextNode] !== true) dfsInnerFunciton(nextNode)
            })
        }

        return dfsVisitedNode
    }
    dfsInnerFunciton(n)
    return dfsVisitedNode
}


function bfs (n) {
    const bfsVisisted = {}
    let bfsVisitedNode = []
    bfsVisisted[n] = true
    bfsVisitedNode.push(n)

    let queue = [n]

    while (queue.length !== 0) {
        const q = queue.shift()

        const nextNodes = connectionMap.get(q)

        if(nextNodes) {
            // console.log(nextNodes)
            nextNodes.forEach(nextNode => {
                if(bfsVisisted[nextNode] !== true) {
                    bfsVisisted[nextNode] = true
                    bfsVisitedNode.push(nextNode)

                    queue.push(nextNode)
                }
            })
        }
    }

    return bfsVisitedNode
}

console.log(...dfs(v))
console.log(...bfs(v))