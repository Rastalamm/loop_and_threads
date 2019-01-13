const printMessages = (endNum) => {
  for (var i = 1; i <= endNum; i++) {
    console.log(determineResponse(i))
  }
}

const determineResponse = (n) => {
  const divisbleByThree = n % 3 === 0
  const divisibleByTwo = n % 2 === 0

  switch (true) {
    case (divisbleByThree && divisibleByTwo):
      return `The number '${n}' is divisible by two and three.`
    case (divisbleByThree):
      return `The number '${n}' is divisible by three.`
    case (divisibleByTwo):
      return `The number '${n}' is even.`
    default:
      return `The number '${n}' is odd.`
  }
}

module.exports = { determineResponse, printMessages }
