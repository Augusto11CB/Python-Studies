'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
'''

from typing import List


class NumArray:
    my_nums = list()

    def __init__(self, nums: List[int]):
        self.my_nums = nums

    def sumRange(self, i: int, j: int, my_other=None) -> int:
        answer = 0
        if i not in range(len(self.my_nums)):
            return  0
        else:
            my_other_answer = sum(self.my_nums[numb] for numb in range(i,j+1))
            for x in range(i,j+1):
                print("it is the x = " + str(x))
                print("it is the self.my_nums[x]" + str(self.my_nums[x]))
                answer = answer + self.my_nums[x]

        print("answer" + str(answer))
        print("my_other_answer" + str(my_other_answer))

        return answer

if __name__ == '__main__':
    object = NumArray([-2, 0, 3, -5, 2, -1])

    print(object.sumRange(0,2))