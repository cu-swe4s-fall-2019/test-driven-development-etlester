import sys
import select


def read_stdin_col(col_num):
    '''This function takes in an integer that references a
    column_number in standard input. it then selects the data in
    that column and returns the column data'''
#    check to see if there is anything in stdin
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        pass
    else:
        print('Error: There is no standard input or input is incorrect form',
              file=sys.stderr)
        sys.exit(1)
#    #read data from standard input
    col_data = []
    for l in sys.stdin:
        A = l.rstrip().split()
        try:
            col_data.append(A[col_num])
        except IndexError:
            print('Error: column number not in dataframe', file=sys.stderr)
            sys.exit(1)
    print(col_data)
    return col_data


test_column = 0
read_stdin_col(test_column)
