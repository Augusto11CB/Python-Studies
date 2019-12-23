#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    number_of_bribes = 0
    q_sorted = q.copy()
    q_sorted.sort()
    for element in q:
        element_index = q.index(element)
        aux_bribes = 0
        for back_element in range(element_index, len(q)):

            if (element > q[back_element]):
                if (aux_bribes < 2):
                    aux_bribes = aux_bribes + 1
                else:
                    return "Too chaotic"

        number_of_bribes = aux_bribes + number_of_bribes

    return number_of_bribes


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
