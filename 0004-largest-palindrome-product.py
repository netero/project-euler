# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(num):
    compare = str(num)
    reversed = compare[::-1]
    return compare==reversed

def findTheBiggestPalindrome(digits):
    lower = 10**(digits-1)
    num1 = 10**digits-1
    
    palindrome = 0
    while num1>=lower:
        num2 = 10**digits-1
        while num2>=lower:
            current = num1*num2
            if isPalindrome(current) and current > palindrome:
                palindrome = current
                break
            num2-=1
        num1-=1
    return palindrome
    


print(findTheBiggestPalindrome(3))