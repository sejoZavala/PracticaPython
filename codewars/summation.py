# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.

# For example (Input -> Output):

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

def summation(num):
    totalSum = 0
    i = 1
    while i <= num:
        totalSum += i
        i +=1
        
    return totalSum

def summationRecursive(num):
    print('incia la funcion con :  %s'%num)

    if num == 1:
        print('se completo el caso base que es:  %s'%num)
        return 1
     
    print('No cumple caso base y se llama la funcion nuevamente pasandole %s (%s - 1) '%(num -1,num) )
    resRec = summationRecursive(num -1)
        
    
    res = num + resRec
    print('valor devuelto por la funcion recurisva es: %s y se suma con lo que inicio en la funcion:  %s, devolviendo %s'%(resRec,num, res))

    return res

if __name__ == "__main__":
    print(summation(2)) # 3 (1 + 2)
    print(summation(8)) # 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
    print(summationRecursive(3))
    