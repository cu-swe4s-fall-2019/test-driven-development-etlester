import sys
import select
import numpy as np
import pandas as pd


def read_stdin_col(col_num):
    '''This function takes in an integer that references a
    column_number in standard input. it then selects the data in
    that column and returns the column data'''
    #check to see if there is anything in stdin
    if select.select([sys.stdin,],[],[],0.0)[0]:
        pass
    else:
        print('Error: There is no standard input', file=sys.stderr)
        sys.exit(1)

    #read data from standard input
    f = sys.stdin.read()
    #split the data by return
    ff = f.strip().split('\n')
    #convert the data to a numpy array
    npff = np.array(ff)
    col_data = []
    for line in npff:
        type = line.split()
        # print(type)
        try:
            working_col_data = int(type[col_num])
        except IndexError:
            print('Error: column number not in dataframe', file=sys.stderr)
            sys.exit(1)
        col_data.append(working_col_data)
        # print(working_col_data)
    # print(col_data)
    return col_data

test_column = 1
read_stdin_col(test_column)
