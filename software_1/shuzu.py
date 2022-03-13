# -*- coding: UTF-8 -*-
"""
找出一个整数数组中子数组之和的最大值
例如：数组[1, -2, 3, 5, -1]，返回8（因为符合要求的子数组是 [3, 5]）
数组[1, -2, 3, -8, 5, 1]，返回6（因为符合要求的子数组是 [5, 1]）;
数组[1, -2, 3,-2, 5, 1]，返回7（因为符合要求的子数组是 [3, -2, 5, 1]）
"""
# num = [1, -2, 3, 5, -1]
# len_num = len(num)
tmep_num = input(" ")
num = [int(n) for n in tmep_num.split()]
max = num[0]
def fun(lists):
    max=lists[0]
    _sum=0
    for i in lists:
        if _sum <0:
            _sum=i
        else:
            _sum+=i
        if _sum>max:
            max=_sum
    return max

print(fun(num))