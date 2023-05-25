const fs = require('fs')

// const input = fs.readFileSync('./dev/stdin').toString().trim().split('\n')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const [L, C] = input[0].split(' ').map(it => parseInt(it))
const alphabets = input[1].split(' ').sort()
// console.log(L,C,alphabets)

const getPermutations = (arr, permLength) => {
    let output = []

    function permutate(rests, perm) {
        if(perm.length === permLength) {
            if(!perm.some(it => it === 'a' || it === 'e' || it === 'i' || it === 'o' || it === 'u')) return
            if(perm.filter(it => it !== 'a' && it !== 'e' && it !== 'i' && it !== 'o' && it !== 'u').length <2) return
            return output.push(perm)
        }

        rests.forEach((v,i)=> {
            const rest = [...rests.slice(i+1)]
            permutate(rest, [...perm, v])
        })
    }

    permutate(arr, [])
    return output
}

const permutations = getPermutations(alphabets, L)
// console.log(permutations)
permutations.forEach(it => console.log(it.join('')))