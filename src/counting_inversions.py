#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
import random

do_print = True
iv_count = 0


def dashes(level) -> str:
    ret = ''
    for i in range(level):
        ret += ret + '+'
    ret += ' '
    return ret


# Complete the countInversions function below.
def merge(arr, temp_array, left_index, mid_index, right_index, level) -> int:
    dsh = dashes(level=level)
    if do_print is True:
        print('{}merge:{}'.format(dsh, level))
    inversion_count = 0
    l = left_index
    r = mid_index + 1

    merged_array_index = left_index
    if do_print is True:
        print('{}left='.format(dsh), end='')
        for i in range(left_index, mid_index + 1):
            print('{}'.format(arr[i]), end=', ')

        print(' :: ', end='')

        print('right=', end='')
        for i in range(mid_index + 1, right_index + 1):
            print('{}'.format(arr[i]), end=', ')
        print('')

    while l <= mid_index and r <= right_index:
        al = arr[l]
        ar = arr[r]
        if al < ar:
            temp_array[merged_array_index] = al
            l += 1
        elif al > ar:
            if inversion_count is 0:
                global iv_count
                inversion_count = mid_index - l
                iv_count += inversion_count
            temp_array[merged_array_index] = ar
            r += 1
        else:
            temp_array[merged_array_index] = al
            merged_array_index += 1
            temp_array[merged_array_index] = ar
            l += 1
            r += 1
        merged_array_index += 1

    while l <= mid_index:
        temp_array[merged_array_index] = arr[l]
        merged_array_index += 1
        l += 1

    while r <= right_index:
        temp_array[merged_array_index] = arr[r]
        merged_array_index += 1
        r += 1

    return inversion_count


def mergeSort(arr, temp_array, left_index, right_index, lr, level: int) -> int:
    dsh = dashes(level=level)
    if do_print is True:
        print('{}mergeSort:{}:{}'.format(dsh, lr, level), end=' // ')
    inversion_count = 0
    tag = (left_index, right_index)

    if do_print is True:
        print('tag=({})'.format(tag), end='')
    if left_index == right_index:
        if do_print is True:
            print('')
        middle = (left_index + right_index) // 2
        #inversion_count += merge(arr, temp_array, left_index, middle, right_index, level=level+1)
    if left_index < right_index:
        middle = (left_index + right_index) // 2
        if do_print is True:
            print('|mid = {}|'.format(middle), end=' ')
            print('')
        inversion_count += mergeSort(arr, temp_array, left_index, middle, lr='L', level=level + 1)
        if do_print is True:
            print('')
        inversion_count += mergeSort(arr, temp_array, middle + 1, right_index, lr='R', level=level + 1)
        inversion_count += merge(arr, temp_array, left_index, middle, right_index, level=level + 1)
        for i in range(left_index, right_index + 1):
            arr[i] = temp_array[i]

    if do_print is True:
        print('{}inversion Count: {},  merged {}: '.format(dsh, level, inversion_count), end='')
        for i in range(left_index, right_index + 1):
            print(temp_array[i], end=', ')
        print(dsh + '\n--')

    return inversion_count


def countInversions(arr) -> int:
    if do_print is True:
        print('countInversions\n')
    temp_array = [0] * len(arr)
    inversion_count = mergeSort(arr, temp_array, 0, len(arr) - 1, lr='root', level=0)
    if do_print is True:
        print('countInversions inversion_count: {}'.format(inversion_count))
    # print(temp_array)
    for i in range(len(arr)):
        arr[i] = temp_array[i]
    return inversion_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())
    t = 0
    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        # fptr.write(str(result) + '\n')
    arr = random.sample(range(100), 100)
    # arr = [9, 7, 1, 2]
    # arr = [9, 5, 8]
    #arr = [1, 1, 1, 2, 2]
    arr = [2, 1, 3, 1, 2]
    inversions = countInversions(arr)
    if do_print is True:
        print(arr)
        print('Inversion Count = %d' % iv_count)
        print(arr)
    # fptr.close()
