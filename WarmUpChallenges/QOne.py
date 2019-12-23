#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'number_in_sequence' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#  3. LONG_INTEGER c
#

def number_in_sequence(primeiro, ultimo, razao):
    myultimo = primeiro + (ultimo - 1) * razao
    print(myultimo)
    if(myultimo == ultimo):
        print("YES")


if __name__ == '__main__':
    entrie = input()
    newEntrie = entrie.split(" ")
    newList = list(map(int,newEntrie))

    print(number_in_sequence(newList[0],newList[1], newList[2]))