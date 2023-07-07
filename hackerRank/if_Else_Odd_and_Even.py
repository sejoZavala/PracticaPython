import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #n = int(input().strip())
    n=5
    print(list(range(5,21)))
    if n%2 == 0 and (n in list(range(2,6)) or n > 20):
        print('Not Weird')
    elif n in list(range(5,21)) :
        print('Not Weird')
    else:
        print('Weird')