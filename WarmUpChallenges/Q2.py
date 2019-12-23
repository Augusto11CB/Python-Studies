#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'number_of_digits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def number_of_digits(n):
    i = 1
    my_number = 0
    while i <= n:
        my_number = my_number + (int(n) - i + 1)
        i = i * 10

    return my_number


if __name__ == '__main__':


    n = int(input())

    print(number_of_digits(n))

