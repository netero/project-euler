# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.
# Result => 233168

def sum_multiples(multiple1, multiple2, until):
    count = 0

    for i in range(multiple1,until):
        if i%multiple1==0 or i%multiple2==0:
            count+=i

    return count

print(sum_multiples(3,5,1000))