import sys
import math


def list_mean(L):
    num_entries = len(L)
    sum_of_data = 0
    for i in range(0, num_entries):
        loop_value = L[i]
        sum_of_data += loop_value
    mean = sum_of_data / num_entries
    return mean


def list_stdev(L):
    num_entries = len(L)
    sum_of_data = 0
    for i in range(0, num_entries):
        loop_value = L[i]
        sum_of_data += loop_value
    mean = sum_of_data / num_entries
    stdev = math.sqrt(sum([(mean-x)**2 for x in L]) / len(L))
    return stdev
