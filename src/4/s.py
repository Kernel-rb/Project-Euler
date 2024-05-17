def largestPalindromeProduct(n) : 
    def isPalindrome(n) : 
        n = str(n)
        if n[::-1] == n :
            return True 
        else : 
            return False 
    arr = []
    for i in range(10**(n-1) , 10**n):
        for j in range(10**(n-1), 10**n):
            arr.append(i * j )
    
    z = []
    for i in arr : 
        if isPalindrome(i) == True : 
            z.append(i)
    return max(z)
print(largestPalindromeProduct(3))