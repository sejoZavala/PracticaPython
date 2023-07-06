
def calcArr(arr):
    repetidos = {}

    for elem in arr:
        if elem in repetidos:
            repetidos[elem] += 1
        else:
            repetidos[elem] = 1

    for val in repetidos.values():
        if val > len(arr) // 2:
            return True
    
    return False

def arrDivCon(arr):
    #dividir problema

    #Resolver de forma recursiva

    #juntar las soluciones
    pass


if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    print(arr, calcArr(arr))

    arr = [1,1,2,4,1,1]
    print(arr, calcArr(arr))

    arr = [1]
    print(arr, calcArr(arr))

    arr = [1,1]
    print(arr, calcArr(arr))


    arr = [1,1]
    print([arr[0],1])