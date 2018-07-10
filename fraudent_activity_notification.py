#!/bin/python3

import math
import os
import random
import re
import sys
import statistics
import bisect

def getMedian(expenditure) -> float:
    expenditure.sort()
    len_expenditure = len(expenditure)
    len_expenditure_mid = len_expenditure // 2
    if len_expenditure % 2:
        return expenditure[len_expenditure_mid]
    else:
        return (expenditure[len_expenditure_mid - 1] + expenditure[len_expenditure_mid]) / 2


# Complete the activityNotifications function below.
def activityNotifications_long(expenditure, d: int)->int:
    start_pos = 0
    notification_count = 0
    size = len(expenditure)
    while (True):
        if size <= d:
            break
        else:
            lst = expenditure[start_pos:start_pos + d]
            med = statistics.median(lst)
            if 2 * med <= expenditure[start_pos + d]:
                notification_count += 1
            start_pos += 1
            size -= 1
    return notification_count


def activityNotifications(expenditure, d: int)->int:
    sorted_arr = []
    notification_count = 0
    for i in range(d):
        bisect.insort(sorted_arr, expenditure[i])

    length_exp = len(expenditure)
    d_mod = d % 2
    d_mid = d // 2
    for i in range(d, length_exp):
        if d_mod == 0:
            median_num = (sorted_arr[d_mid] + sorted_arr[d_mid-1]) / 2.0
        else:
            median_num = sorted_arr[d_mid]

        if expenditure[i] >= 2 * median_num:
            notification_count += 1

        remove_item_pos = bisect.bisect(sorted_arr, expenditure[i - d]) -1
        sorted_arr.pop(remove_item_pos)
        bisect.insort(sorted_arr, expenditure[i])

    return notification_count


if __name__ == '__main__':
    #os.environ['OUTPUT_PATH'] = "test"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    #print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
