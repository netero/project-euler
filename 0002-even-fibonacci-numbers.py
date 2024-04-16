# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def sumEvenFibonacci(limit):
    count = 0
    previous = 0
    currentFibonacci = 1

    while(currentFibonacci<=limit):
        if(currentFibonacci%2==0):
            count+=currentFibonacci
        temp=currentFibonacci
        currentFibonacci=currentFibonacci+previous
        previous=temp
    
    return count

print(sumEvenFibonacci(4000000))