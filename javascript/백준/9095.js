const fs = require("fs")
const { resourceLimits } = require("worker_threads")

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

