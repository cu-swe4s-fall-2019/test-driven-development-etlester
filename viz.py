import data_viz
import get_data
import argparse
import sys


def initialize():
    parser = argparse.ArgumentParser(
                description='Pass parameters',
                prog='visualize data')

    parser.add_argument('--out_file',
                        type=str,
                        help='Name of the output plot',
                        required=True)

    parser.add_argument('--col_num',
                        type=int,
                        help='The column number',
                        required=True)
    parser.add_argument('--plot_type',
                        type=str,
                        help='''The type of plot you want.
                             histogram, boxlot, or combo''',
                        required=True)

    args = parser.parse_args()
    return args


def main():
    #   pull in arguments from initialize using argparse
    args = initialize()
    #   pull data from stdin using read_std_in

    try:
        col_data = get_data.read_stdin_col(args.col_num)
    except ValueError:
        print("Error: column number is out of bounds")
        sys.exit(1)
    if args.plot_type == 'boxplot':
        data_viz.boxplot(col_data, args.out_file)
    elif args.plot_type == 'histogram':
        data_viz.histogram(col_data, args.out_file)
    elif args.plot_type == 'combo':
        data_viz.combo(col_data, args.out_file)
    else:
        print("""The plot_type is incorrect. Please enter one of the following:
        histogram, boxplot, or combo""")
        sys.exit(1)


if __name__ == '__main__':
    main()
