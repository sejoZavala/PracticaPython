def positive_sum(arr):
    if len(arr) == 0 or all(map(lambda x: x < 0, arr) ):
        return 0
    return sum(filter(lambda x: x>0 ,arr))


if __name__ == "__main__":
    print(positive_sum([1,2,3,4,5,-5])) 