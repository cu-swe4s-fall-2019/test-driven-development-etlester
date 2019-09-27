import sys
import matplotlib
import matplotlib.pyplot as plt
import math_lib
matplotlib.use('Agg')


def boxplot(L, out_file_name):
    '''This method takes two arguments:
    L is an array of input data and out_file_name is the name of the plot
    you would like to save.
    This function makes a boxplot of the data, L, adds the mean and standard
    deviation as a title, and saves the image to the name passed
    in out_file_name.'''
    data_mean = math_lib.list_mean(L)
    data_stdev = math_lib.list_stdev(L)
    summary_stats = [data_mean, data_stdev]
    headder = ['mean: ' + str(data_mean), 'stdev: ' + str(data_stdev)]
    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.boxplot(L)
    plt.title(headder, loc='center')
    plt.savefig(out_file_name, bbox_inches='tight')


def histogram(L, out_file_name):
    '''This method takes two arguments:
    L is an array of input data and out_file_name is the name of the plot
    you would like to save.
    This function makes a histogram of the data, L, adds the mean and standard
    deviation as a title, and saves the image to the name passed
    in out_file_name.'''
    data_mean = math_lib.list_mean(L)
    data_stdev = math_lib.list_stdev(L)
    summary_stats = [data_mean, data_stdev]
    headder = ['mean: ' + str(data_mean), 'stdev: ' + str(data_stdev)]
    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(L)
    plt.title(headder, loc='center')
    plt.savefig(out_file_name, bbox_inches='tight')


def combo(L, out_file_name):
    '''This method takes two arguments:
    L is an array of input data and out_file_name is the name of the plot
    you would like to save.
    This function makes both a histogram and a boxplot of the data, L,
    dds the mean and standard deviation as a title, and saves the image
    to the name passed in out_file_name.'''
    data_mean = math_lib.list_mean(L)
    data_stdev = math_lib.list_stdev(L)
    summary_stats = [data_mean, data_stdev]
    headder = ['mean: ' + str(data_mean), 'stdev: ' + str(data_stdev)]
    width = 5
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 2, 1)
    ax.boxplot(L)
    ax = fig.add_subplot(1, 2, 2)
    ax.hist(L)
    plt.title(headder, loc='right')
    plt.savefig(out_file_name, bbox_inches='tight')


if __name__ == '__main__':
    main()
