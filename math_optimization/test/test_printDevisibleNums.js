const assert = require('assert')
const P = require('../printDevisibleNums.js')

describe('Test the different values and their responses', function () {
  it('should return odd for an input of 1', function () {
    const input = 1
    const res = P.determineResponse(input)
    assert.equal(res, `The number '${input}' is odd.`)
  })

  it('should return even for an input of 2', function () {
    const input = 2
    const res = P.determineResponse(input)
    assert.equal(res, `The number '${input}' is even.`)
  })

  it('should return divisible by 3 for an input of 3', function () {
    const input = 3
    const res = P.determineResponse(input)
    assert.equal(res, `The number '${input}' is divisible by three.`)
  })

  it('should return divisible by 2 and 3 for an input of 6', function () {
    const input = 6
    const res = P.determineResponse(input)
    assert.equal(res, `The number '${input}' is divisible by two and three.`)
  })
})
