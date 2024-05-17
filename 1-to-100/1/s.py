def multiple_of_3or_5(number) : 
    counter = 0 
    for i in range(0 , number + 1) : 
        if i % 3 == 0 or i % 5 == 0  :
            counter += i 
    return counter


print(multiple_of_3or_5(1000))
print(multiple_of_3or_5(10))
print(multiple_of_3or_5(49))
print(multiple_of_3or_5(8456))
print(multiple_of_3or_5(19564))