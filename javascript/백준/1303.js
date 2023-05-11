const fs = require("fs")

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [n,m] = input[0].split(' ')
const boxes = input.slice(1).map(it => it.split(''))

// console.log(doubleList)

let queue = []
let visited = []
for (let index = 0; index < m; index++) visited.push([])
for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
        visited[i].push(false)
    }
}

let myPower = 0
let enemyPower = 0

boxes.forEach((box, i) => box.forEach((soldier, j)=> {
    // console.log("============")
    let soldierCount = 0
    if (visited[i][j] === false) {
        queue.push([i,j])
        visited[i][j] = true

        const dir = [[-1, 0], [1,0], [0,1], [0,-1]]
        while(queue.length !== 0) {
            // console.log(queue)
            const [x,y] = queue.shift()
            // console.log(x,y)

            // 병사수 계산
            soldierCount += 1
            /////////////////////

            // 북동남서 붙어있는 병사 체크
            dir.forEach(([px, py]) => {
                const [nx, ny] = [x+px, y+py]
                if(nx >= 0 && nx < m && ny >= 0 && ny < n) {
                    if(visited[nx][ny] === false && boxes[nx][ny] === soldier) {
                        visited[nx][ny] = true
                        queue.push([nx,ny])
                    }
                }
            })
            /////////////////////
        }
        // console.log(soldier, soldierCount)
        const power = soldierCount * soldierCount
        if(soldier === 'W') myPower += power
        else enemyPower += power
    }
    // console.log("==========")
}))

console.log(myPower, enemyPower)