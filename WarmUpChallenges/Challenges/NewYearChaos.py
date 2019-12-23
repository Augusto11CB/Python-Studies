#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q:list):
    number_of_bribes = 0
    q_sorted = q.copy()
    q_sorted.sort()
    for element in q:
        print("element" + str(element))
        original_index = q_sorted.index(element)
        currently_index = q.index(element)
        print("currently_number" + str(currently_index))
        print("original_index" + str(original_index))
        is_bribe_invalid = original_index - currently_index
        print(is_bribe_invalid)
        if is_bribe_invalid > 2:
            return "Too chaotic"
        else:
            if currently_index < original_index:

                number_of_bribes = number_of_bribes + is_bribe_invalid

    return number_of_bribes


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
