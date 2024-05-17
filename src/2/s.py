def fiboEvenSum(n) : 
    a =  1 
    b = 2 
    c = a + b
    counter = 2  
    while c <= n : 
        if c % 2 == 0 : 
            counter += c 
        a = b  
        b = c
        c = a + b  
    return counter
        
print(fiboEvenSum(10))
print(fiboEvenSum(34))
print(fiboEvenSum(60))
print(fiboEvenSum(1000))
print(fiboEvenSum(100000))
print(fiboEvenSum(4000000))
