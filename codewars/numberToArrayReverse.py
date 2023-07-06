def digitize(n):
    if n == 0:
        return [0]
    arr =  [int(num) for num in str(n)[::-1]]
    return arr


if __name__ == "__main__":
    print(digitize(123456789)) # [9,8,7,6,5,4,3,2,1]