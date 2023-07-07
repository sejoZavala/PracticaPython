def reverse_seq(n):
    if n==1:
        return [1]
    
    data = [n] + reverse_seq(n-1)
    
    return data

if __name__ == '__main__':
        print ([2]+[1])
        print(reverse_seq(5))