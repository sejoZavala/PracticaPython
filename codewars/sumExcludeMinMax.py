def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    return sum(sorted(arr)[1:-1])


if __name__ == "__main__":
    print(sum_array([1,20,3,4,5,-5])) 
