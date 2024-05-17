def smallestMulitple(n) : 
    nombre_premier = [] 
    plus_grand_puissance = []
    for z in range(2, n):
        divisible = False
        for i in range(2, n):
            for j in range(2, n):
                if z == i * j:
                    divisible = True
                    break
            if divisible:
                break
        if not divisible:
            nombre_premier.append(z)

    for i in nombre_premier:
        puissance = 1
        while i ** puissance < n:
            puissance += 1
        plus_grand_puissance.append(i ** (puissance - 1))
    
    res = 1 
    for i in plus_grand_puissance:
        res *= i
    return res


print(smallestMulitple(20))