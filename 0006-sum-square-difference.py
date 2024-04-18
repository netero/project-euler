# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumSquareDifference(qty):
    sumSquares = 0
    squareOfSum = 0
    for i in range(1,qty+1):
        sumSquares += i**2
        squareOfSum +=i
    squareOfSum**=2
    return squareOfSum-sumSquares

print(sumSquareDifference(100))