#!/usr/bin/env python
# coding=utf-8
# Python使用的是3.4.3，缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用

# m, n, steps = map(int, input().split())
# m = abs(m)
# n = abs(n)
# if m + n > steps:
#     print("No")
# else:
#     rest = steps - m - n
#     if rest % 2 == 0:
#         print("Yes")
#     else:
#         print("No")
#
# import math
# x= int(input().strip())
# n = int(math.sqrt(2*x+0.25)-1.5)
# print(x-2*n)

# import sys
#
# inputs = list(map(lambda x: list(map(int, x.strip().split(' '))), sys.stdin.readlines()))
#
#
# def slice(inputs):
#     i = 0
#     while True:
#         n, m = inputs[i]
#         if n == 0 and m == 0:
#             break
#         yield inputs[i + 1:i + 1 + m]
#         i += m + 1
#
#
# for data in slice(inputs):
#     relation = {1}
#
#     while True:
#         old_len = len(relation)
#         for (m, n) in data:
#             if m in relation or n in relation:
#                 relation.add(m)
#                 relation.add(n)
#         if old_len == len(relation):
#             break
#     print(len(relation) - 1)

# count, operation_count = map(int, input().split())
# boxes = [0]*count
# for i in range(count):
#     boxes[i] = int(input().strip())
#
# for i in range(operation_count):
#     operation, num1, num2 = map(int, input().split())
#     if operation == 1:
#         boxes[num1-1] = num2
#     elif operation == 2:
#         print(sum(boxes[num1-1: num2]))
#     elif operation == 3:
#         print(max(boxes[num1-1: num2]))

# count = int(input().strip())
#
# result = 0
# for i in range(count):
#     left_item, right_item = map(int, input().split())
#     result+= left_item if left_item <= right_item else right_item
#
# print(result)

person_count, question_count = map(int, input().split())
question_solved = [0] * question_count
for i in range(person_count):
    left, right = map(int, input().split())
    for j in range(left, right + 1):
        question_solved[j-1] += 1

print(max(question_solved))
