target = 3
li = [1, 2, 3, 4, 5]

dictionary = {}

for i in range(len(li)):
    num = li[i]  
    difference = target - num  
    
    if difference in dictionary:
        
        print("Результат:", (dictionary[difference], i))
        break 

    dictionary[num] = i
