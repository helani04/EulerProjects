def reverse(n):
    reversed = 0
    while n > 0:
        reversed = reversed * 10 + n % 10
        n = n / 10
    return reversed


def isPalindromic(n):
    return(n == reverse(n))


a = 999
largestPalindrome = 0
while a >= 100:
    b = 999
    while b >= a:
        if a*b<=largestPalindrome:
            break
        if isPalindromic(a * b):
            largestPalindrome = a * b
            print(a*b)
        b = b - 1
    a = a - 1
print(largestPalindrome)
