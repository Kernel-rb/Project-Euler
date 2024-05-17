def sumSquareDifference(n) :
    a =  0 
    b = 0 
    for i in range(1 ,n+1) :
        a += i*i
    for i in range(1 , n+1): 
        b += i
    
    c = b**2
    z = c - a
    return z
     

print(sumSquareDifference(100))
