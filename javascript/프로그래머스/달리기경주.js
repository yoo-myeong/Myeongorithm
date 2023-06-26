const playerToNum = {}

const numToPlayer = {}

const setPlayerToNum = (players) => {
    players.forEach((v, i) => {
        playerToNum[v] = i
    })
}

const setNumToPlayer = (players) => {
    players.forEach((v, i) => {
        numToPlayer[i] = v
    })
}

const updateMap = (playerName) => {
    const numOfPlayer = playerToNum[playerName]

    const numOfNextPlayer = numOfPlayer -1
    const nextPlayerName = numToPlayer[numOfNextPlayer]

    // console.log(numOfPlayer, numOfNextPlayer, nextPlayerName)

    playerToNum[playerName] = numOfPlayer - 1
    playerToNum[nextPlayerName] = numOfNextPlayer + 1

    numToPlayer[numOfPlayer] = nextPlayerName
    numToPlayer[numOfNextPlayer] = playerName
}

function solution(players, callings) {
    let answer = [];

    try {
        setPlayerToNum(players)
        setNumToPlayer(players)

        // console.log(JSON.stringify(playerToNum))
        // console.log(JSON.stringify(numToPlayer))

        callings.forEach(playerName => {
            updateMap(playerName)
        })

        // console.log(JSON.stringify(playerToNum))
        // console.log(JSON.stringify(numToPlayer))

        answer = players.map((v, i) => {
            return numToPlayer[i]
        })

    } catch(e) {
        // console.log(e)
    }

    return answer;
}
