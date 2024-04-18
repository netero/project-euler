# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#1,2,3,4,5,6,7,8,9,10

def find(num):
    result = 1
    while True:
        isMultiple = True
        for i in range(1,num+1):
            if result%i!=0:
                isMultiple = False
                break
        if isMultiple:
            return result
        result+=1

print(find(20))