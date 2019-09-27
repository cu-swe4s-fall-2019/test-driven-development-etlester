import sys
import math


def list_mean(L):
    num_entries = len(L)
    sum_of_data = 0
    for i in range(0, num_entries):
        loop_value = L[i]
        if isinstance(loop_value, int):
            sum_of_data += loop_value
        elif isinstance(loop_value, str):
            print("Error: Input is a string, not an integer")
            raise TypeError
            sys.exit(1)
        elif isinstance(loop_value, float):
            print("Error: Input is a float, not an integer")
            raise TypeError
            sys.exit(1)
        else:
            print("Error: Input format is incorrect")
            raise TypeError
    mean = sum_of_data / num_entries
    return mean


def list_stdev(L):
    num_entries = len(L)
    sum_of_data = 0
    for i in range(0, num_entries):
        loop_value = L[i]
        if isinstance(loop_value, int):
            sum_of_data += loop_value
        elif isinstance(loop_value, str):
            print("Error: Input is a string, not an integer")
            raise TypeError
            sys.exit(1)
        elif isinstance(loop_value, float):
            print("Error: Input is a float, not an integer")
            raise TypeError
            sys.exit(1)
        else:
            print("Error: Input format is incorrect")
            raise TypeError
    mean = sum_of_data / num_entries
    stdev = math.sqrt(sum([(mean-x)**2 for x in L]) / len(L))
    return stdev


# if __name__ == '__main__':
#     main()
